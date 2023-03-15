from scipy.stats import pearsonr
import numpy as np

# Define the data
data = np.array([
    [25, 50, 75, 100, 125, 150],
    [12.3, 9.1, 6.4, 2.3, -1.2, -6.1],
    [10.8, 8.9, 4.6, 3.4, -0.9, -4.7],
    [7.9, 5.7, 3.5, 1.8, -0.5, -0.88],
    [6.2, 4.5, 2.7, 1.1, -1.2, -1.8],
    [10.1, 6.5, 4.8, 1.52, -0.96, -1.6],
    [11.5, 10.3, 8.1, 6.8, -0.32, -0.45]
])

# Calculate the correlation matrix
corr_matrix, _ = pearsonr(data[1], data[0]), pearsonr(data[2], data[0]), pearsonr(data[3], data[0]), pearsonr(data[4], data[0]), pearsonr(data[5], data[0]), pearsonr(data[6], data[0])

# Print the correlation matrix
print(corr_matrix)
