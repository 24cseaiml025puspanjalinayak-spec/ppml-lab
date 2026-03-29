#WAP to create an integer list of 20 elements increase the odd elements by 5.
s=[]
x = int(input("Enter the number of elements: "))
for i in range(x):
    s.append(int(input("Enter the element: ")))
for i in range(x):
    if s[i]%2 != 0:
        s[i] += 5 

print(s)