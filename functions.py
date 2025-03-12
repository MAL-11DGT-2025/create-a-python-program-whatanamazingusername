def greeting():
    print("Hi chat")

def greeting_w_name(name):
    print(f"Hi {name}, welcome to the chat.")

def addition(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def divide(a, b):
    print(a / b)


#asks what operation and numbers
operation = input("What operation do you want to use? \n ( +, -, *, / )")
a = input("Enter your first number: ")
b = input("Enter your second number: ")

if operation == "+":
    addition(a, b)
elif operation == "-":
    subtract(a, b)
elif operation == "*":
    multiply(a, b)
elif operation == "/":
    divide(a, b)






#addition(45786874 , 762197321)
#addition(45678 , 9877821563)
#addition(123456789 , 987654321)

#subtract(457324 , 3284327)
#subtract(87893427 , 328462)
#subtract(3289432 , 932786432)

#greeting()
#greeting_w_name("Human")
#greeting_w_name("Peter")
#greeting_w_name("Guy")

