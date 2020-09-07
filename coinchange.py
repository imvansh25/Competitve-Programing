# recursive
def coinchange(n,coins):
    if n==0:
        return 0
    min_steps = float('inf')
    for i in coins:
        if n-i >=0:
            sub_step = coinchange(n-i,coins)
            min_steps = min(min_steps,sub_step+1)
    return min_steps

## top-down approch
def coinchangetd(n,coins,dp_array):
    if n==0:
        return 0
    min_steps = float('inf')
    for i in coins:
        if n-i >=0:
            sub_step = coinchangetd(n-i,coins,dp_array)
            min_steps = min(min_steps,sub_step+1)
    dp_array[n]=min_steps
    return dp_array[n]

def coinchangebottomup(n,coins):
    dp = [0 for i in range(n+1)]
    for value in range(1,len(dp)):
        min_steps = float('inf')
        for coin in coins:
            if value-coin>=0:
                sub_step = dp[value-coin]
                min_steps = min(min_steps,sub_step+1)
        dp[value]=min_steps
    return dp[n]
print(coinchangebottomup(15,[1,7,10]))

