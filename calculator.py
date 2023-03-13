def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except:
        print("float division by zero")


def power(x, y):
    return x ** y

def remainder(x, y):
    return x % y

def select_op(choice):
    if(choice == "#"):
        return -1
    elif(choice == "$"):
        return 0
    elif(choice in ('+', '-', '*', '/', '^', '%', '#', '$')):
        while True:
            num1=str(input("Enter first number: "))
            print(num1)
            if num1.endswith('$'):
                return 0
            if num1.endswith('#'):
                return -1
            try:
                x1=float(num1)
                break
            except:
                print("Not a valid number,please try again")
                continue
        while True:
            num2=str(input("Enter second number: "))
            print(num2)
            if num2.endswith('$'):
                return 0
            if num2.endswith('#'):
                return -1
            try:
                x2=float(num2)
                break
            except:
                print("Not a valid number,please try again")
                continue
        if choice == '+':
            print(x1, "+", x2, "=", add(x1, x2))

        elif choice == '-':
            print(x1, "-", x2, "=", subtract(x1, x2))

        elif choice == '*':
            print(x1, "*", x2, "=", multiply(x1, x2))

        elif choice == '/':
            print(x1, "/", x2, "=", divide(x1, x2))

        elif choice == '^':
            print(x1, "^", x2, "=", power(x1, x2))

        elif choice == '%':
            print(x1, "%", x2, "=", remainder(x1, x2))
        else:
            print("Something Went Wrong")
    else:
        print("Unrecognized operation")

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if(select_op(choice) == -1):
        print("Done. Terminating")
        exit()


