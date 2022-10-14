import math
n=int(input())
res=int(math.sqrt(n))
if int(res**2)==n:
    print('True')
else:
    print('False')