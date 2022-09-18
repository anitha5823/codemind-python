n=int(input())
r=0
rev=0
sq1=0
sq2=0
t=n
while n != 0:
    r=n%10
    rev=rev*10+r
    n=n//10
sq1=str(t**2)
sq2=str(rev**2)
if sq1[-1]==sq2[0] and sq1[0]==sq2[-1]:
    print('True')
else:
    print('False')