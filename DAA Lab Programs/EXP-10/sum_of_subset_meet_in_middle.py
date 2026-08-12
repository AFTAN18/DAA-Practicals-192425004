from itertools import combinations
def subset_sums(a):
    s=[]
    for r in range(len(a)+1):
        for c in combinations(a,r):
            s.append(sum(c))
    return s
def meet_middle(arr,target):
    n=len(arr)
    L=subset_sums(arr[:n//2]);R=sorted(subset_sums(arr[n//2:]))
    best=0
    for x in L:
        lo,hi=0,len(R)-1
        while lo<=hi:
            m=(lo+hi)//2
            if x+R[m]<=target:
                best=max(best,x+R[m]);lo=m+1
            else:hi=m-1
    return best
print(meet_middle([45,34,4,12,5,2],42))
