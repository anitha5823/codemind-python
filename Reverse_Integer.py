n=int(input())
lst=list(str(n))
if lst[-1] =='0':
    lst.pop()
lst.reverse()
if lst[-1]== '-':
    lst.pop()
    lst.insert(0,'-')
    print("".join(lst))
else:
    print("".join(lst))