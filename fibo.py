## recursive method

def fibo_rec(n):
    if n==0 or n==1:
        return n
    
    return fibo_rec(n-1)+fibo_rec(n-2)


## Dp top down approch

def fibo_TD(n,dp_arr):
    if n==0 or n==1:
        return n
    if dp_arr[n]!=0:
        return dp_arr[n]
    dp_arr[n] = fibo_TD(n-1,dp_arr)+fibo_TD(n-2,dp_arr)
    return dp_arr[n]

## Bottom -Up approch
def fibo_Bu(n):
    dp_arr = [0 for i in range(n+1)]
    dp_arr[1]=1

    for i in range(2,n+1):
        dp_arr[i]=dp_arr[i-1]+dp_arr[i-2]
    return dp_arr[n]

## Bottom -Up approch with space opimization
def fibo_Bu_2(n):
    dp_arr = [0 for i in range(3)]
    dp_arr[1]=1

    for i in range(2,n+1):
        dp_arr[-1] = dp_arr[0]+dp_arr[1]
        dp_arr[0]=dp_arr[1]
        dp_arr[1]=dp_arr[-1]
    return dp_arr[-1]


print(fibo_Bu_2(10))