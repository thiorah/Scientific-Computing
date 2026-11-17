
import numpy as np
from scipy.linalg import lu_factor, lu_solve

print("TASK 07: GAUSSIAN ELIMINATION AND LU DECOMPOSITION")

# PART 1: Create the coefficient matrix
A = np.array([
    [4.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 3.0]
])

# PART 2: Create different measurement sets
measurement_sets = [
    np.array([15.0, 10.0, 10.0]),
    np.array([16.0, 11.0, 9.0]),
    np.array([14.0, 12.0, 11.0])
]

print("\n--- Coefficient Matrix A ---")
print(A)

# PART 3: Perform LU decomposition once
lu, piv = lu_factor(A)

print("\n--- LU Factorization ---")
print("Combined LU factors:")
print(lu)

print("Pivot information:")
print(piv)

# PART 4: Solve each measurement set using the same factors
print("\n--- Solutions Using LU Decomposition ---")

for i, b in enumerate(measurement_sets, start=1):

    x = lu_solve((lu, piv), b)

    # Verify the solution
    residual = b - A @ x

    print(f"\nMeasurement Set {i}")
    print("Input values:", b)
    print("Solution:", np.round(x, 4))
    print("Calculated values:", np.round(A @ x, 4))
    print("Residual norm:", np.linalg.norm(residual))

# PART 5: Compare with direct solution
direct_solution = np.linalg.solve(A, measurement_sets[0])

lu_solution = lu_solve((lu, piv), measurement_sets[0])

print("\n--- Direct Solution Comparison ---")
print("LU solution:", np.round(lu_solution, 4))
print("Direct solution:", np.round(direct_solution, 4))

# PART 6: Modify one measurement set
modified_b = np.array([18.0, 12.0, 10.0])

modified_solution = lu_solve((lu, piv), modified_b)

print("\n--- Modified Experiment ---")
print("Modified measurements:", modified_b)
print("New solution:", np.round(modified_solution, 4))
print("Verification:", np.round(A @ modified_solution, 4))
