#WAP to create a function that prints the first 15 terms of the fibonacci series without using recursion

def fibonacci(n):
    a,b = 0,1
    print(a,b,end=" ")
    for i in range(2,n):
        c = a + b
        print(c,end=" ")
        a = b
        b = c
n = int(input("Enter the number of terms you want to print: "))
print(f"The Fibonacci series of first {n} terms are :")
fibonacci(n)