A=[list(map(int,input().split())) for _ in range(2)]
B=[list(map(int,input().split())) for _ in range(2)]
a,b=A[0];c,d=A[1]
e,f=B[0];g,h=B[1]
p1=a*(f-h);p2=(a+b)*h;p3=(c+d)*e;p4=d*(g-e)
p5=(a+d)*(e+h);p6=(b-d)*(g+h);p7=(a-c)*(e+f)
print(p5+p4-p2+p6,p1+p2)
print(p3+p4,p1+p5-p3-p7)
