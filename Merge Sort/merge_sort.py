def m(a):
    if len(a)>1:
        h=len(a)//2;l=a[:h];r=a[h:]
        m(l);m(r);i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:a[k]=l[i];i+=1
            else:a[k]=r[j];j+=1
            k+=1
        while i<len(l):a[k]=l[i];i+=1;k+=1
        while j<len(r):a[k]=r[j];j+=1;k+=1
a=list(map(int,input().split()))
m(a)
print(*a)
