import numpy as np

lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)

print("Original List:", lst)
print("One-dimensional NumPy array:", arr)

import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

import numpy as np

arr = np.zeros(10)
print(arr)

arr[5] = 11
print(arr)

import numpy as np

arr = np.arange(12, 38)
print(arr)

import numpy as np

arr = np.array([1, 2, 3, 4])
float_arr = arr.astype(float)

print("Original array")
print(arr)
print("Converted to float:")
print(float_arr)

import numpy as np

C = np.array([0, 12, 45.21, 34, 99.91])
F = C * 9/5 + 32

print("Values in Fahrenheit degrees:")
print(F)

print("\nValues in Centigrade degrees:")
print((F - 32) * 5/9)
import numpy as np

C = np.array([0, 12, 45.21, 34, 99.91])
F = C * 9/5 + 32

print("Values in Fahrenheit degrees:")
print(F)

print("\nValues in Centigrade degrees:")
print((F - 32) * 5/9)

import numpy as np

arr = np.array([10, 20, 30])
updated = np.append(arr, [40, 50, 60, 70, 80, 90])

print("Original array:")
print(arr)

print("After appending:")
print(updated)

import numpy as np

data = np.random.rand(10)

print("Array:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))

import numpy as np

arr = np.random.rand(10, 10)

print("Minimum:", arr.min())
print("Maximum:", arr.max())

import numpy as np

arr = np.random.rand(3, 3, 3)
print(arr)


