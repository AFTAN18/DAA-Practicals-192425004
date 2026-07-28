arr = list(map(int, input("Enter array: ").split()))

m = arr[0]

for i in arr:
    if i > m:
        m = i

print(m)
