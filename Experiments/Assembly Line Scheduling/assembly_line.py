a = [
    [4, 5, 3, 2],
    [2, 10, 1, 4]
]
t = [
    [7, 4, 5],
    [9, 2, 8]
]
e = [10, 12]
x = [18, 7]
n = 4
dp = [[0] * n for _ in range(2)]
dp[0][0] = e[0] + a[0][0]
dp[1][0] = e[1] + a[1][0]
for j in range(1, n):
    dp[0][j] = min(
        dp[0][j - 1] + a[0][j],
        dp[1][j - 1] + t[1][j - 1] + a[0][j]
    )
    dp[1][j] = min(
        dp[1][j - 1] + a[1][j],
        dp[0][j - 1] + t[0][j - 1] + a[1][j]
    )
answer = min(
    dp[0][n - 1] + x[0],
    dp[1][n - 1] + x[1]
)
print("Minimum time:", answer)
