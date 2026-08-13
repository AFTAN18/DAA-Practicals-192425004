def q(a):
    if len(a)<=1:return a
    p=a[len(a)//2]
    return q([x for x in a if x<p])+[x for x in a if x==p]+q([x for x in a if x>p])
a=list(map(int,input().split()))
print(*q(a))
