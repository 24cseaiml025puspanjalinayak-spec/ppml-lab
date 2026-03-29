#1.create a numpy array with element 10,20,30,40
import numpy as np
arr=np.array([10,20,30,40])
print(arr)



#2.create a 2d array and display its shape and dimension
import numpy as np
arr=np.array([[1,2,3],[5,6,7]])
print(arr)
print("Shape:",arr.shape)
print("dimension:",arr.ndim)



#3.create array using zeros(), ones(), empty() functions
import numpy as np
zeros_array=np.zeros((2,3))
ones_array=np.ones((3,4))
empty_array=np.empty((2,2))
print("Zeros Array:\n",zeros_array)
print("Ones Array:\n",ones_array)
print("Empty Array:\n",empty_array)



#7.find mean , median , standard deviation of a numpy array
import numpy as np
arr=np.array([1,2,3,4,5])
mean=np.mean(arr)
median=np.median(arr)
std_dev=np.std(arr)
print("Mean:",mean)
print("Median:",median)
print("Standard Deviation:",std_dev)