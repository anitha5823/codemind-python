n=int(input())
t=0
num=n
while n != 0:
    s=1
    r=n%10
    for i in range(r,0,-1):
        s=s*i
    t=t+s
    n=n//10
if t==num:
    print('The number',num,'is a strong number')
else:
    print('The number',num,'is not a strong number')