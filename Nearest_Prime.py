#next prime
t=int(input())
for i in range(1,t+1):
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
    
    if a-n < n-b:
        print(a)
    else:
        print(b)