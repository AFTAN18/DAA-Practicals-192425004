INF = 9999
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
n = len(cost)
dp = [[INF] * n for _ in range(1 << n)]
dp[1][0] = 0
for mask in range(1 << n):
    for u in range(n):
        if mask & (1 << u):
            for v in range(n):
                if not (mask & (1 << v)):
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] = min(
                        dp[new_mask][v],
                        dp[mask][u] + cost[u][v]
                    )
full = (1 << n) - 1
ans = INF
for i in range(n):
    ans = min(ans, dp[full][i] + cost[i][0])
print("Minimum TSP cost:", ans)
