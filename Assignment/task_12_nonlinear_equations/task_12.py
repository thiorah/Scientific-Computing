
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root
import os

print("TASK 12: POLYNOMIAL AND NONLINEAR EQUATION SOLVING")


# PART 1: Original problem
# Circle: x^2 + y^2 = 4
# Parabola: y = x^2 - 1

def equations(z):
    x, y = z

    return [
        x**2 + y**2 - 4,
        y - (x**2 - 1)
    ]


# PART 2: Solve using different initial guesses

initial_guesses = [
    [1.0, 1.0],
    [-1.0, 1.0]
]

solutions = []

print("\n--- ORIGINAL CIRCLE AND PARABOLA ---")

for guess in initial_guesses:

    solution = root(equations, guess)

    print("\nInitial guess:", guess)
    print("Intersection:", np.round(solution.x, 6))
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)

    if solution.success:
        solutions.append(solution.x)


# PART 3: Verify the solutions
print("\n--- SOLUTION VERIFICATION ---")

for i, point in enumerate(solutions, start=1):

    x, y = point

    circle_value = x**2 + y**2
    parabola_value = x**2 - 1

    print(f"\nIntersection {i}")
    print("Circle left-hand side:", round(circle_value, 6))
    print("Parabola y-value:", round(parabola_value, 6))
    print("Maximum residual:",
          np.max(np.abs(equations(point))))


# PART 4: Modify the circle
# Original radius = 2
# Modified radius = 3

def modified_equations(z):
    x, y = z

    return [
        x**2 + y**2 - 9,
        y - (x**2 - 1)
    ]


print("\n--- MODIFIED CIRCLE ---")

modified_guesses = [
    [2.0, 2.0],
    [-2.0, 2.0]
]

modified_solutions = []

for guess in modified_guesses:

    solution = root(modified_equations, guess)

    print("\nInitial guess:", guess)
    print("Intersection:", np.round(solution.x, 6))
    print("Residuals:", modified_equations(solution.x))
    print("Converged:", solution.success)

    if solution.success:
        modified_solutions.append(solution.x)


# PART 5: New real-world application
# Example: Finding where a parabolic signal path
# crosses a circular wireless coverage boundary.
# The coverage radius is 3 units.

print("\n--- WIRELESS COVERAGE APPLICATION ---")

for i, point in enumerate(modified_solutions, start=1):

    x, y = point

    print(f"Boundary intersection {i}:")
    print(f"x = {x:.6f}, y = {y:.6f}")


# PART 6: Plot the original and modified curves

x_values = np.linspace(-2.5, 2.5, 400)

circle_y_positive = np.sqrt(
    np.maximum(0, 4 - x_values**2)
)

circle_y_negative = -circle_y_positive

modified_circle_positive = np.sqrt(
    np.maximum(0, 9 - x_values**2)
)

modified_circle_negative = -modified_circle_positive

parabola_y = x_values**2 - 1

os.makedirs(
    "task_12_nonlinear_equations/output",
    exist_ok=True
)

plt.figure(figsize=(9, 6))

plt.plot(
    x_values,
    circle_y_positive,
    label="Original circle"
)

plt.plot(
    x_values,
    circle_y_negative
)

plt.plot(
    x_values,
    modified_circle_positive,
    linestyle="--",
    label="Modified circle"
)

plt.plot(
    x_values,
    modified_circle_negative,
    linestyle="--"
)

plt.plot(
    x_values,
    parabola_y,
    label="Parabola"
)

if solutions:
    original_points = np.array(solutions)
    plt.scatter(
        original_points[:, 0],
        original_points[:, 1],
        label="Original intersections"
    )

if modified_solutions:
    new_points = np.array(modified_solutions)
    plt.scatter(
        new_points[:, 0],
        new_points[:, 1],
        label="Modified intersections"
    )

plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.title("Circle and Parabola Intersections")
plt.axhline(0, linewidth=0.6)
plt.axvline(0, linewidth=0.6)
plt.grid(True)
plt.legend()

plt.savefig(
    "task_12_nonlinear_equations/output/intersections.png"
)

plt.show()

print("\nGraph saved successfully.")
print("Task 12 completed successfully.")
