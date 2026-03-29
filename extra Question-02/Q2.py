def fibo(a,b, count):
    if count == 0:
        return
    print(a, end=", ")
    fibo(b,a+b,count-1)

def fibo2(n):
    if n <= 1:
        return n
    return fibo2(n-1)+fibo2(n-2)


n = int(input("Enter the number of terms to be printed :- "))
fibo(0,1,n)
print("\n",fibo2(n-1))