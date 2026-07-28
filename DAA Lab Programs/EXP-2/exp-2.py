nums1 = list(map(int, input("Enter nums1: ").split()))
nums2 = list(map(int, input("Enter nums2: ").split()))

a1 = 0
a2 = 0

for i in nums1:
    if i in nums2:
        a1 += 1

for i in nums2:
    if i in nums1:
        a2 += 1

print([a1, a2])
