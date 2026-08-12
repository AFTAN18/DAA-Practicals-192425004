def min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    mid = (low + high) // 2
    min1, max1 = min_max(arr, low, mid)
    min2, max2 = min_max(arr, mid + 1, high)
    minimum = min(min1, min2)
    maximum = max(max1, max2)
    return minimum, maximum
arr = list(map(int, input("Enter elements: ").split()))
minimum, maximum = min_max(arr, 0, len(arr) - 1)
print("Minimum:", minimum)
print("Maximum:", maximum)
