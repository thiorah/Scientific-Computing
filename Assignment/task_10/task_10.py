
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
import os

print("TASK 10: BISECTION AND FIXED-POINT METHODS")

# PART 1: Original heat-balance model
# Find the temperature where heat balance equals zero.

def heat_balance(T):
    return T - 25 - 10 * np.exp(-T / 20)


# PART 2: Bisection method
solution = root_scalar(
    heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10
)

bisection_result = solution.root

# PART 3: Fixed-point method
# Rearranged equation:
# T = 25 + 10 * exp(-T / 20)

def g(T):
    return 25 + 10 * np.exp(-T / 20)


T = 30.0
history = [T]

for _ in range(100):
    T_new = g(T)
    history.append(T_new)

    if abs(T_new - T) < 1e-10:
        break

    T = T_new

fixed_point_result = history[-1]

# Display original results
print("\n--- ORIGINAL HEAT-BALANCE MODEL ---")
print(f"Bisection temperature: {bisection_result:.6f} C")
print(f"Fixed-point temperature: {fixed_point_result:.6f} C")
print("Fixed-point iterations:", len(history) - 1)

print("Bisection verification:", heat_balance(bisection_result))
print("Fixed-point verification:", heat_balance(fixed_point_result))


# PART 4: Change one parameter
# Increase base temperature from 25 to 30.

def modified_heat_balance(T):
    return T - 30 - 10 * np.exp(-T / 20)


modified_solution = root_scalar(
    modified_heat_balance,
    bracket=[20, 50],
    method="bisect",
    xtol=1e-10
)

print("\n--- MODIFIED EXPERIMENT ---")
print("New base temperature parameter: 30 C")
print(
    f"New equilibrium temperature: "
    f"{modified_solution.root:.6f} C"
)


# PART 5: New related real-world application
# Model a refrigeration chamber with a different
# base temperature and heat contribution.

def cooling_balance(T):
    return T - 30 - 8 * np.exp(-T / 25)


cooling_solution = root_scalar(
    cooling_balance,
    bracket=[20, 50],
    method="bisect",
    xtol=1e-10
)

print("\n--- REFRIGERATION CHAMBER APPLICATION ---")
print(f"Equilibrium temperature: {cooling_solution.root:.6f} C")


# PART 6: Plot the original heat-balance function
temperatures = np.linspace(20, 40, 300)

os.makedirs("task_10_bisection_fixed_point/output", exist_ok=True)

plt.figure(figsize=(9, 5))

plt.plot(
    temperatures,
    heat_balance(temperatures),
    label="Heat-balance function"
)

plt.axhline(0, linewidth=0.8)
plt.axvline(
    bisection_result,
    linestyle="--",
    label="Equilibrium temperature"
)

plt.xlabel("Temperature (C)")
plt.ylabel("Heat-balance function")
plt.title("Heat-Balance Equilibrium Temperature")
plt.legend()
plt.grid(True)

plt.savefig(
    "task_10_bisection_fixed_point/output/equilibrium.png"
)

plt.show()

print("\nGraph saved successfully.")
print("Task 10 completed successfully.")
