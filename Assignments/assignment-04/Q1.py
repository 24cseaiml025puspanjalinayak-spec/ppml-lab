# WAP to print the second largest and second smallest element is a list of 10 integers without using sort function.

arr = []
x = int(input("Enter the number of elements: "))
for i in range(x):
    m = int(input("Enter the element: "))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k] > arr[k+1]:
            arr[k],arr[k+1] = arr[k+1],arr[k]
print("The sorted array is: ", arr)
print("The second largest element is ", arr[-2])
print("The second smallest element is ", arr[1])