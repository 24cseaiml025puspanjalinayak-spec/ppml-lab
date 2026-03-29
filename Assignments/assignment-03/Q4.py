# WAP tp check whether the string is symmetrical or palindrome.

x = input("Enter a string :")
z = (str(str(x)[::-1]))
if x == z:
    print("It is a palindrome")
else:
    print("It is a not palindrome")