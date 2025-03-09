def convert(number, choice):
    if choice == "f":
        result = number - 32 * (5/9)
    elif choice == "c":
        result = number * (9/5) + 32
    print(result)

temp = input("Do you want to convert \n a)fahrenheit to celsius \n b)celsius to fahrenheit? \n\n- ")
number = int(input("What is the tempurature you would like to convert? \n\n-"))

f_to_c = ["fahrenhiet to celsius", "a", "a)"]
c_to_f = ["celsius", "b", "b)"]

if temp in f_to_c:
    convert(number, "f")
elif temp in c_to_f:
    convert(number, "c")