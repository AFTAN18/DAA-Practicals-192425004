a=sorted(map(int,input().split()))
a=list(a)
x=int(input())
l,h=0,len(a)-1
while l<=h:
    m=(l+h)//2
    if a[m]==x:print(m);break
    if a[m]<x:l=m+1
    else:h=m-1
else:print(-1)
