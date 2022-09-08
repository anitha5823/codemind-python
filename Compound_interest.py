import math
p,r,t=map(float,input().split())
ci=0
ci =  p * (pow((1 + r / 100), t))
print('%.2f'%ci,)