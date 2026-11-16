
import numpy as np
import matplotlib.pyplot as plt
import os

print("TASK 08: ITERATIVE METHODS FOR LINEAR SYSTEMS")

# PART 1: Create the temperature model
A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

# Boundary temperatures: left = 100 C, right = 20 C
b = np.array([100., 0., 0., 0., 20.])

# PART 2: Jacobi method
def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)

    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        x_new = (b - R @ x) / D

        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)

        if error < tol:
            return x_new, errors

        x = x_new

    return x, errors


# PART 3: Gauss-Seidel method
def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        old = x.copy()

        for i in range(len(b)):
            x[i] = (
                b[i]
                - A[i, :i] @ x[:i]
                - A[i, i+1:] @ old[i+1:]
            ) / A[i, i]

        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)

        if error < tol:
            return x, errors

    return x, errors


# PART 4: Solve the original temperature problem
x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)

# Direct solution for comparison
x_exact = np.linalg.solve(A, b)

print("\n--- Original Temperature Model ---")
print("Jacobi temperatures:", np.round(x_j, 4))
print("Gauss-Seidel temperatures:", np.round(x_gs, 4))
print("Direct solution:", np.round(x_exact, 4))

print("\n--- Iteration Information ---")
print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))
print("Jacobi final error:", err_j[-1])
print("Gauss-Seidel final error:", err_gs[-1])

# PART 5: Modify the boundary temperatures
# New left boundary = 80 C
# New right boundary = 40 C

modified_b = np.array([80., 0., 0., 0., 40.])

modified_j, modified_errors = jacobi(A, modified_b)
modified_gs, modified_gs_errors = gauss_seidel(A, modified_b)

print("\n--- Modified Temperature Model ---")
print("New boundary values:", modified_b)
print("Jacobi result:", np.round(modified_j, 4))
print("Gauss-Seidel result:", np.round(modified_gs, 4))

# PART 6: New related real-world application
# A cooling panel with left boundary = 60 C
# and right boundary = 20 C.

cooling_b = np.array([60., 0., 0., 0., 20.])

cooling_result, cooling_errors = gauss_seidel(A, cooling_b)

print("\n--- Cooling Panel Application ---")
print("Boundary values:", cooling_b)
print("Estimated interior temperatures:",
      np.round(cooling_result, 4))

# PART 7: Plot convergence
plt.figure(figsize=(9, 5))

plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")

plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence of Iterative Temperature Solution")
plt.legend()
plt.grid(True)

# Save the graph inside the task folder
os.makedirs("task_08_iterative_linear/output", exist_ok=True)

plt.savefig(
    "task_08_iterative_linear/output/convergence.png"
)

print("\nConvergence graph saved successfully.")

plt.show()
