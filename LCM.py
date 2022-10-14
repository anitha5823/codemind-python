a,b=map(int,input().split())
p=0
if a<b:
    p=b
else:
    p=a
while True:
    if p%a==0 and p%b==0:
        print(p)
        break
    p=p+1