def k(x,y):
    if x<10 or y<10:return x*y
    n=max(len(str(x)),len(str(y)));m=n//2
    a,b=x//10**m,x%10**m
    c,d=y//10**m,y%10**m
    z0=k(b,d);z1=k(a+b,c+d);z2=k(a,c)
    return z2*10**(2*m)+(z1-z2-z0)*10**m+z0
print(k(int(input()),int(input())))
