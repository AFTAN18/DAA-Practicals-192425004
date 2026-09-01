n = int(input("Enter number of keys: "))

keys = list(map(int, input("Enter keys: ").split()))
freq = list(map(int, input("Enter frequencies: ").split()))

dp = [[0 for _ in range(n)]
      for _ in range(n)]

for i in range(n):
    dp[i][i] = freq[i]


def sum_freq(i, j):
    return sum(freq[i:j+1])


for length in range(2, n + 1):

    for i in range(n - length + 1):

        j = i + length - 1

        dp[i][j] = float('inf')

        total = sum_freq(i, j)

        for root in range(i, j + 1):

            left = dp[i][root - 1] if root > i else 0
            right = dp[root + 1][j] if root < j else 0

            dp[i][j] = min(
                dp[i][j],
                left + right + total
            )

print("Minimum cost of Optimal BST =", dp[0][n-1])
