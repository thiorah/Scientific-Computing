
import numpy as np

print("TASK 06: SOLUTION OF SYSTEMS OF LINEAR EQUATIONS")

# PART 1: Original server resource problem
# x = number of Type A servers
# y = number of Type B servers

# Type A uses 4 CPU units and 8 GB memory
# Type B uses 2 CPU units and 12 GB memory
# Total usage: 20 CPU units and 72 GB memory

A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])

b = np.array([20.0, 72.0])

# Solve the simultaneous equations
solution = np.linalg.solve(A, b)

print("\n--- Original Problem ---")
print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")

# PART 2: Verify the solution
verification = A @ solution
residual = b - verification

print("\n--- Verification ---")
print("Calculated resource usage:", verification)
print("Expected resource usage:", b)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))

# PART 3: Change the input values
# New observed usage: 24 CPU units and 96 GB memory

modified_b = np.array([24.0, 96.0])

modified_solution = np.linalg.solve(A, modified_b)

print("\n--- Modified Experiment ---")
print(f"New Type A servers: {modified_solution[0]:.0f}")
print(f"New Type B servers: {modified_solution[1]:.0f}")

# PART 4: New related real-world application
# A different server configuration in a data centre.
# Type A uses 6 CPU units and 8 GB memory.
# Type B uses 2 CPU units and 16 GB memory.
# Total usage: 18 CPU units and 64 GB memory.

new_A = np.array([
    [6.0, 2.0],
    [8.0, 16.0]
])

new_b = np.array([18.0, 64.0])

new_solution = np.linalg.solve(new_A, new_b)

print("\n--- New Real-World Application ---")
print(f"Type A servers: {new_solution[0]:.0f}")
print(f"Type B servers: {new_solution[1]:.0f}")

# Verify the new application
new_verification = new_A @ new_solution

print("Calculated resource usage:", new_verification)
print("Expected resource usage:", new_b)
