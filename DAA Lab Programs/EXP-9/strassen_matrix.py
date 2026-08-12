def strassen(A,B):
    a,b=A[0];c,d=A[1]
    e,f=B[0];g,h=B[1]
    p1=a*(f-h);p2=(a+b)*h;p3=(c+d)*e
    p4=d*(g-e);p5=(a+d)*(e+h)
    p6=(b-d)*(g+h);p7=(a-c)*(e+f)
    return [[p5+p4-p2+p6,p1+p2],[p3+p4,p1+p5-p3-p7]]
A=[[1,7],[3,5]]
B=[[6,8],[4,2]]
for r in strassen(A,B): print(r)
