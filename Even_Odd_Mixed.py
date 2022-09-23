n=int(input())
r=e=o=m=0
t=n
while n != 0:
    r=n%10
    if r % 2 == 0:
        e+=1
    elif r % 2 !=0:
        o+=1
    else:
         m+=1
    n=n//10
t=str(t)
l=len(t)
if e == l:
    print('Even')
elif o == l:
    print('Odd')
else:
    print('Mixed')