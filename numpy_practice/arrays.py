import numpy as np

# creating arrays
a = np.array([1, 2, 3, 4])            # 1d
m = np.array([[1, 2, 3], [4, 5, 6]])  # 2d
print("ndim:", m.ndim, "shape:", m.shape, "size:", m.size, "dtype:", m.dtype)

print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.full((2, 3), 7))
print(np.arange(0, 10, 2))    # start, stop, step
print(np.linspace(0, 1, 5))   # 5 evenly spaced points
print(np.eye(3))              # identity matrix

# indexing and slicing
print("reversed:", a[::-1])
print("second row:", m[1], "| last column:", m[:, -1])

# reshape, transpose, matrix product
print(a.reshape(2, 2))
print(m.T)
print(m.dot(m.T))
