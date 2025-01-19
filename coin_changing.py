def min_coins_w_memo(amt,coins):
    # Initialize tables:
    # T: Table to store the minimum no. of coins for each amount.
    # S: Table to store the first coin value that leads to the minimum no. of coins for each amount.
    T = [float('inf')] * (amt + 1)
    S = [float('inf')] * (amt + 1)

    T[0] = 0
    S[0] = 0
    for i in range(1,amt+1):
        for j in range(len(coins)):
            remainder = i-coins[j]
            if remainder >= 0:
                #print(f'i={i};j={j};T[i]={T[i]};coins[j]={coins[j]};1+T[remainder]={1+T[remainder]}')
                if T[i] > 1 + T[remainder]:
                    T[i] = 1 + T[remainder]
                    S[i] = coins[j]

        
    #reconstruct
    changes = []
    curr_amt = amt
    
    while curr_amt > 0:
        changes.append(S[curr_amt])
        curr_amt -= S[curr_amt]

    #print(T)
    return T[amt],changes


coins = [100,50,20,10,5]

print(min_coins_w_memo(230,coins))
                      