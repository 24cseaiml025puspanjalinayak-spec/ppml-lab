n = int(input("Enter a number :- "))
if n <= 0:
    print("Enter a positive number.")
else:
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i
    if total == n :
        print("The number is a perfect number.")
    else:
        print("The number is not a perfect number.")