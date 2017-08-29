def rec_coin(target,coins):
    min_coins = target
    if target in coins:
        return 1
    else:
        # For every coin value that is <= target
        for i in [c for c in coins if c<= target]:
            # add a coin count + recursive
            num_coins = 1 + rec_coin(target-i,coins)
            # reset minimum if new num_coins < min_coins
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

def rec_coin_dyn(target,coins,known_results):
    #default output to target
    min_coins = target
    #Base case
    if target in coins:
        known_results[target] = 1
        return 1
    #return known result if it's greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        for i in [c for c in coins if c<= target]:
            num_coins = 1 + rec_coin_dyn(target-i,coins,known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                # Reset known result
                known_results[target] = min_coins
                
    return min_coins

target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)

rec_coin_dyn(target,coins,known_results)

