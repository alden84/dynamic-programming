# Rod cutting problem:
# For a rod of size L, we know that it can be cut in different sizes and each size has a corresponding price if sold.
# The question is how to cut the rod to achieve maximum revenue?
# This is a classic problem that can be solved using dynamic programming due to overlapping subproblems and optimal substructure properties.

def max_rev_w_memo(L, sizes, prices):
    # Initialize tables:
    # T: Table to store the maximum revenue for each rod length from 0 to L.
    # S: Table to store the size of the first cut that leads to the maximum revenue for each rod length.
    T = [0] * (L + 1)
    S = [0] * (L + 1)

    # Fill the T and S tables iteratively for each rod length.
    for i in range(len(T)): 
        for j in range(len(sizes)): 
            # Find maximum revenue for length `i` based on all possible cuts.
            remainder = i - sizes[j]
            if remainder >= 0:
                # Calculate revenue: price of the first cut + maximum revenue of the remainder (from the T table).
                rev = prices[j] + T[remainder]
                if rev > T[i]:  # Update if the current cut yields better revenue.
                    T[i] = rev
                    S[i] = sizes[j]  # Store the size of the first cut for reconstruction.

    # Reconstruct the cuts based on the S table:
    # Start from the full rod length and trace back through the cuts stored in S.
    l = L
    cuts = []
    while l >= 0 and S[l] > 0:
        cuts.append(S[l])  # Add the first cut for the current length.
        l -= S[l]  # Reduce the remaining length by the size of the cut.

    # Return the maximum revenue and the sequence of cuts.
    return T[L], cuts


# Test the function with an example:
# L: Total rod length.
# sizes: Available sizes of cuts.
# prices: Corresponding prices for each cut size.
L = 110
sizes = [1, 3, 5, 10, 30, 50, 75]
prices = [0.1, 0.2, 0.4, 0.9, 3.1, 5.1, 8.2]

# Call the function and print the results:
max_rev, cuts = max_rev_w_memo(L, sizes, prices)

print(f"Max revenue is: {max_rev}")  # Expected: The maximum revenue for rod length 110.
print(f"Cuts to achieve max revenue: {cuts}")  # Expected: A sequence of cuts that maximizes revenue.

