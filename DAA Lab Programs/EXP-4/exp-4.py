nums = list(map(int, input("Enter array: ").split()))
k = int(input("Enter k: "))

count = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and (i * j) % k == 0:
            count += 1

print(count)
