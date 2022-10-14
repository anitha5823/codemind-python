n=int(input())
c=0
a=map(int,input().split())
for i in a:
    c+=i
while(n):
    if c%n==0:
        print(n)
        break
    n-=1
