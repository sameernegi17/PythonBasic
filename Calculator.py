def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        print("division not possible")
        return 0;
    else:
        return a / b

def subtraction(a,b):
    return a - b


def calc(a,b,operator):
    if (operator == '+'):
        return add(a,b)
    elif(operator == "-"):
        return subtraction(a,b)
    elif(operator == "*"):
        return multiply(a,b)
    elif(operator == "/"):
        return divide(a,b)
    else:
        print("operator Not found")
        return -1

a =  int(input("Enter First Number"))
b = int(input("Enter Second Number"))
operator = input("Enter the operator")

print(calc(a,b,operator))