def median_of_medians(arr,k):
    if len(arr)<=5:
        return sorted(arr)[k-1]
    groups=[arr[i:i+5] for i in range(0,len(arr),5)]
    medians=[sorted(g)[len(g)//2] for g in groups]
    pivot=median_of_medians(medians,(len(medians)+1)//2)
    left=[x for x in arr if x<pivot]
    mid=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    if k<=len(left):
        return median_of_medians(left,k)
    elif k<=len(left)+len(mid):
        return pivot
    return median_of_medians(right,k-len(left)-len(mid))
arr=[12,3,5,7,19]
print(median_of_medians(arr,2))
