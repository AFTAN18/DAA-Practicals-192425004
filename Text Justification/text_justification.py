def wordWrap(words, width):
    n = len(words)
    dp = [999] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        length = 0
        for j in range(i, 0, -1):
            length += len(words[j - 1])
            if i != j:
                length += 1
            if length > width:
                break
            cost = 0 if i == n else (width - length) ** 2
            dp[i] = min(dp[i], dp[j - 1] + cost)
    return dp[n]
words = ["This", "is", "a", "text", "justification", "example"]
width = 16
print("Minimum cost:", wordWrap(words, width))
