nums = list(map(int, input("Enter array: ").split()))

ans = 0

for i in range(len(nums)):
    s = set()
    for j in range(i, len(nums)):
        s.add(nums[j])
        ans += len(s) ** 2

print(ans)
