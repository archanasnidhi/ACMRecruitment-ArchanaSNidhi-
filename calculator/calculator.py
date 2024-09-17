import re
import sys
x=input("Enter the mathematical expression:")
y = re.findall(r'\d+|\+|\-|\*|\/|\^|\(|\)', x)
def prc(l):
    if "^" in l:
        index=l.index("^")
        expo(index,l)
    elif "*" in l:
        index=l.index("*")
        prod(index,l)
    elif "/"in l:
        index=l.index("/")
        div(index,l)
    elif "-"in l:
        index=l.index("-")
        sub(index,l)
    elif "+" in l:
        index=l.index("+")
        add(index,l)
    return l

def add(index,l):
    a=float(l[index-1])
    b=float(l[index+1])
    ans=a+b
    l[index-1]=ans
    del l[index+1]
    del l[index]
    return l

def sub(index,l):
    a=float(l[index-1])
    b=float(l[index+1])
    ans=a-b
    l[index-1]=ans
    del l[index+1]
    del l[index]
    return l
def prod(index,l):
    a=float(l[index-1])
    b=float(l[index+1])
    ans=a*b
    l[index-1]=ans
    del l[index+1]
    del l[index]
    print(l)
def div(index,l):
    a=float(l[index-1])
    b=float(l[index+1])
    try:
        ans=a/b
        l[index-1]=ans
        del l[index+1]
        del l[index]
        return l
    except ZeroDivisionError:
        print("Division by zero is not valid")
        print("zero division error")
        sys.exit()
def expo(index,l):
    a=float(l[index-1])
    b=float(l[index+1])
    ans=a**b
    l[index-1]=ans
    del l[index+1]
    del l[index]
    return l
def para():
    global y
    a=y.index("(")
    b=y.index(")")
    z=y[a+1:b]
    for i in range(b,a,-1):
        del y[i]
    while len(z)>1:
        f=prc(z)
    y[a]=f[0]
while len(y)>1:
    if "(" in y:
        para()
    prc(y)
print(y[0])
