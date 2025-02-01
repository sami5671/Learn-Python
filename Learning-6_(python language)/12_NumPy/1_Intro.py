"""
Step:1 To install the NumPy write pip install numpy

Step:2 Import the numpy module

"""

import numpy as np

arr = np.array([1, 2, 3, 4])
print("Array is: ", arr)
print(np.__version__)
print(type(arr))

arr2 = np.array((1, 2, 3, 4))
print("Tuple Array is: ", arr2)


zero_D_arr = np.array(42)
print("Zero D Array is: ", zero_D_arr)

one_D_arr = np.array([1, 2, 3, 4])
print("One D Array is: ", one_D_arr)

two_D_arr = np.array([[1, 2], [3, 4]])
print("Two D Array is: ")
print(two_D_arr)

three_D_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("Three D Array is:")
print(three_D_arr)


# check the array dimensions
print("Number of dimension is: ", zero_D_arr)
print("Number of dimension is: ", one_D_arr.ndim)
print("Number of dimension is: ", two_D_arr.ndim)
print("Number of dimension is: ", three_D_arr.ndim)

# can create custom dimensions
custom_dimension = np.array([1, 2, 3, 4, 5], ndmin=5)
print("Custom dimension is: ", custom_dimension.ndim)
