n=int(input())
s1=0
s=list(str(n))
s.sort()
res=list(set(s))
res.sort()
if(s==res):
    print('Unique Number')
else:
    print('Not Unique Number')