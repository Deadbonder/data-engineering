import numpy as np

k = np.array([5, 1, 4, 2, 4, 3])

# broadcasting: the scalar is applied to every element
print(k + 10, k * 2)

# statistics
print("mean:", np.mean(k), "median:", np.median(k), "std:", np.std(k))

# boolean masking
mask = k > 2
print("mask:", mask)
print("filtered:", k[mask])
print("indices where >2:", np.where(k > 2))
print("1 if >2 else 0:", np.where(k > 2, 1, 0))

print("unique:", np.unique(k))
print("sorted:", np.sort(k))

# random numbers
rng = np.random.default_rng(0)
print("uniform [0,1):", rng.random(3))
print("standard normal:", rng.standard_normal(3))
