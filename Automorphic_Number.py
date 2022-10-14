n=int(input())
a=n**2
l=len(str(n))
end=a%pow(10,l)
if n==end:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number') 