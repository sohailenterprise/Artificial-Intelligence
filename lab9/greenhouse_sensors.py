import numpy as np

np.random.seed(7)
readings = np.random.randint(20, 41, size=(6, 3))
print(readings)

# (1) Mean of each sensor
mean = readings.mean(axis=0)
print("Mean per sensor:", mean)

# (2) Standardize with broadcasting
std = readings.std(axis=0)
normalized = (readings - mean) / std
print("Normalized column means:", np.round(normalized.mean(axis=0), 10) + 0.0)

# (3) Hour in which each sensor peaked
print("Hour of max per sensor:", readings.argmax(axis=0))

# (4) Append the mean row below the readings
with_mean = np.vstack([readings, mean])
print(with_mean.shape)

# (5) Reproducibility: re-seed and regenerate
np.random.seed(7)
readings2 = np.random.randint(20, 41, size=(6, 3))
print("Reproducible:", np.array_equal(readings, readings2))