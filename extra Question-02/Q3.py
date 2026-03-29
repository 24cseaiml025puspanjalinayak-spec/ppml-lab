def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

n = int(input("Enter a number :- "))
print(f"The sum of first {n} natural number is {sum(n)}")