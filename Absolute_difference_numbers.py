n,i=map(int,input().split())
n=str(n)
l=len(n)
print(abs(int(n[:i])-int(n[l-i:])))