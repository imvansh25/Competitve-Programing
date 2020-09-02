"""
Ques - 
given a no n
reduce the number to 1
by 3 options 
    1. If n%2==0 => n/=2
    2. If n%3==0 => n/=3
    3. n=n-1
"""

## using recursion

def min_steps(n):
    if n==1:
        return 0
    option_1,option_2,option_3=float('inf'),float('inf'),float('inf')
    if n%2==0:
        option_1 = min_steps(n/2)
    if n%3==0:
        option_2=min_steps(n/3)
    option_3 = min_steps(n-1)

    return min(min(option_3,option_2),option_1)+1

## using top-down approch

def min_steps_td(n,dp_arr):
    if n==1:
        return 0
    if dp_arr[n]!=0:
        return dp_arr[n]
    option_1,option_2,option_3=float('inf'),float('inf'),float('inf')
    if n%2==0:
        option_1 = min_steps(n/2)
    if n%3==0:
        option_2=min_steps(n/3)
    option_3 = min_steps(n-1)

    dp_arr[n]=min(min(option_3,option_2),option_1)+1
    return dp_arr[n]

## using bottom-up approch

def min_steps_bu(n):
    dp_arr = [0 for i in range(n+1)]

    for i in range(2,n+1):
        option_1,option_2,option_3=float('inf'),float('inf'),float('inf')
        if i%2==0:
            option_1 = dp_arr[int(i/2)]
        if i%3==0:
            option_2=dp_arr[int(i/3)]
        option_3 = dp_arr[int(i-1)]
        dp_arr[i]=min(min(option_3,option_2),option_1)+1
    return dp_arr[n]

print(min_steps_bu(10))
