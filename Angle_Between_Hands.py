h,m=map(int,input().split(":"))
if h== 12:
    h=0
if m== 60:
    h+=1
    m=0
if h>12:
    h=h-12
a=0.5*(h*60+m)
m=6*m
res=abs(a-m)
print(min(360-res,res))