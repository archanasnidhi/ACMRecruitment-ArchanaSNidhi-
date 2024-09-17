import re
import sys

def imp(l):
    while True:
        if "^" in l:
            index = l.index("^")
            l = exponent(index, l)
        elif "*" in l:
            index = l.index("*")
            l = multiplication(index, l)
        elif "/" in l:
            index = l.index("/")
            l = division(index, l)
        elif "-" in l:
            index = l.index("-")
            l = subtraction(index, l)
        elif "+" in l:
            index = l.index("+")
            l = addition(index, l)
        else:
            break
    return l

def addition(index, l):
    a = float(l[index-1])
    b = float(l[index+1])
    ans = a + b
    l[index-1] = ans
    del l[index+1]
    del l[index]
    return l

def subtraction(index, l):
    a = float(l[index-1])
    b = float(l[index+1])
    ans = a - b
    l[index-1] = ans
    del l[index+1]
    del l[index]
    return l

def multiplication(index, l):
    a = float(l[index-1])
    b = float(l[index+1])
    ans = a * b
    l[index-1] = ans
    del l[index+1]
    del l[index]
    return l

def division(index, l):
    a = float(l[index-1])
    b = float(l[index+1])
    try:
        ans = a / b
        l[index-1] = ans
        del l[index+1]
        del l[index]
        return l
    except ZeroDivisionError:
        print("Division by zero is not valid")
        sys.exit()

def exponent(index, l):
    a = float(l[index-1])
    b = float(l[index+1])
    ans = a ** b
    l[index-1] = ans
    del l[index+1]
    del l[index]
    return l

def evaluate_expression(expression):
    y = re.findall(r'\d+|\+|\-|\*|\/|\^|\(|\)', expression)
    
    def paranthesis():
        nonlocal y  
        while '(' in y:
            a = y.index("(")
            b = y.index(")")
            z = y[a+1:b]
            
            result = imp(z)
            
            y = y[:a] + [result[0]] + y[b+1:]

    def imp(l):
        while True:
            if "^" in l:
                index = l.index("^")
                l = exponent(index, l)
            elif "*" in l:
                index = l.index("*")
                l = multiplication(index, l)
            elif "/" in l:
                index = l.index("/")
                l = division(index, l)
            elif "-" in l:
                index = l.index("-")
                l = subtraction(index, l)
            elif "+" in l:
                index = l.index("+")
                l = addition(index, l)
            else:
                break
        return l

    
    paranthesis()
    result = imp(y)
    return result[0]

x = input("Enter the equation to be evaluated: ")
result = evaluate_expression(x)
print(result)
