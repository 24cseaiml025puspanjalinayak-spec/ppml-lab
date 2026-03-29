def min_ele(l,i,min):
    if i == len(l):
        print(min)
        return
    elif l[i] < min:
        min_ele(l,i+1,l[i])
    else :
        min_ele(l,i+1,min)

l = [3,2,5,1,7]
print("The minimum element in the list is ", end="")
min_ele(l,1,l[0])