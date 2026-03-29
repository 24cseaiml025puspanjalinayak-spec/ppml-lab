# WAP to find the factorial of a number.

x = int(input("Enter a number :- "))
factorial = 1
if x < 0:
    print("It is a negative number.")
elif x == 0:
    print(f"The factorial of {x} is : {factorial}")
else:
    for i in range(2,x+1):
        factorial *= i
    print(f"The factorial of {x} is : {factorial}")