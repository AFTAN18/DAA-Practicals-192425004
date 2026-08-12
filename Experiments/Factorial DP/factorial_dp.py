def factorial(n):
    dp=[1]*(n+1)
    for i in range(2,n+1):
        dp[i]=dp[i-1]*i
    return dp[n]
print(factorial(5))
