l=int(input())
u=int(input())
for i in range(l,u+1):
    num=i
    c=0
    r=1
    t=list(str(i))
    t=len(t)
    while i!=0:
        r=i%10
        if r!=0:
            if num%r==0:
                c+=1
        else:
            pass
        i=i//10
    if c==t:
        print(num,end=' ')
    else:
        continue