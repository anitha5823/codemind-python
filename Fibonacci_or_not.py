n=int(input())
lst=[]
f1,f2,f3=0,1,0
for i in range(1,n):
    f3=f1+f2
    f1=f2
    f2=f3
    lst.append(f3)
if n in lst:
    print('True')
else:
    print('False')