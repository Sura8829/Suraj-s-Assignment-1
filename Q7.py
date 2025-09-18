a = int(input("Please enter a number: "))
b= int(input("Please enter another number: "))
c =input("What do you wanna do?")

if c == "+":
    print(a+b) 
elif c == "-":
    print(a-b)
elif c == "*":  
    print(a*b)
elif c == "/":  
    print(a/b)
else:
    print("Invalid operation")  