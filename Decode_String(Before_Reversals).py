t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    s=input()
    for i in range(n,0,-1):
        s=s[i-1::-1]+s[i:]
    print(s)