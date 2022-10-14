n=int(input())
a=n+1
while True:
    p=True
    for i in range(2,int(a**0.5)+1):
        if a % i==0:        
            p=False
            break
    if p == True:
        break
    else:
        a=a+1

#previous prime
b=n
while True:
    p=True
    for i in range(2,int(b**0.5)+1):
        if b % i==0:        
            p=False
            break
    if p == True:
        break
    else:
        b=b-1
d1=a-n
d2=n-b
if d1 < d2:
    print(d1)
else:
    print(d2)