t=int(input())
for i in range(1,t+1):
    c=0
    l,r=map(int,input().split())
    for j in range(l,r+1):
        n=list(str(j))
        if n[-1]=='2' or n[-1]=='3' or n[-1]=='9':
            c+=1
    print(c)