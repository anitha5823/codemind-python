n=input()
s=""
c=0
for i in n:
    if i=='6' and c!=1:
        c+=1
        s+='9'
    else:
        s=s+i
print(s)