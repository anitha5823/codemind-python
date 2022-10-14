n=int(input())
c=0
a=map(int,input().split())
for i in a:
    c+=i
if c%2==0:
    print(1)
else:
    print(0)