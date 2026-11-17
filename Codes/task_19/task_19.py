
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from pathlib import Path

# ==========================================
# TASK 19: NUMERICAL OPTIMIZATION
# ==========================================

# Automatically create output folder
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ==========================================
# PART 1: ORIGINAL CLOUD SERVER PROBLEM
# ==========================================

# Server costs
cost_A = 12
cost_B = 18

# Server processing capacities
capacity_A = 100
capacity_B = 170

# Required minimum capacity
required_capacity = 1000


# Objective function: minimize total cost
def cost_function(z):
    x, y = z
    return cost_A * x + cost_B * y


# Capacity constraint
def capacity_constraint(z):
    x, y = z
    return capacity_A * x + capacity_B * y - required_capacity


constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}

# Servers cannot have negative allocations
bounds = [(0, None), (0, None)]

# Find the optimal allocation
solution = minimize(
    cost_function,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x

total_cost = cost_function(solution.x)
total_capacity = capacity_A * x + capacity_B * y

print("PART 1: ORIGINAL CLOUD SERVER OPTIMIZATION")
print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total processing capacity: {total_capacity:.2f}")
print(f"Minimum operating cost: {total_cost:.2f}")


# ==========================================
# PART 2: MODIFY REQUIRED CAPACITY
# ==========================================

# Increase required capacity from 1000 to 1200
modified_required_capacity = 1200

def modified_capacity_constraint(z):
    x, y = z
    return (
        capacity_A * x
        + capacity_B * y
        - modified_required_capacity
    )


modified_solution = minimize(
    cost_function,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints={
        "type": "ineq",
        "fun": modified_capacity_constraint
    }
)

modified_x, modified_y = modified_solution.x

modified_cost = cost_function(modified_solution.x)

modified_total_capacity = (
    capacity_A * modified_x
    + capacity_B * modified_y
)

print("\nPART 2: MODIFIED CLOUD SERVER PROBLEM")
print("Optimization success:", modified_solution.success)
print(f"New required capacity: {modified_required_capacity}")
print(f"Type A allocation: {modified_x:.3f}")
print(f"Type B allocation: {modified_y:.3f}")
print(f"Total processing capacity: {modified_total_capacity:.2f}")
print(f"New minimum operating cost: {modified_cost:.2f}")


# ==========================================
# PART 3: NEW APPLICATION
# CYBERSECURITY LOG PROCESSING
# ==========================================

# A security monitoring system needs enough
# capacity to process incoming security logs.

# Two types of processing resources
log_cost_A = 10
log_cost_B = 16

log_capacity_A = 80
log_capacity_B = 150

required_log_capacity = 900


# Minimize the cost of log processing resources
def log_cost_function(z):
    x, y = z
    return log_cost_A * x + log_cost_B * y


# Ensure sufficient log processing capacity
def log_capacity_constraint(z):
    x, y = z
    return (
        log_capacity_A * x
        + log_capacity_B * y
        - required_log_capacity
    )


log_solution = minimize(
    log_cost_function,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints={
        "type": "ineq",
        "fun": log_capacity_constraint
    }
)

log_x, log_y = log_solution.x

log_total_cost = log_cost_function(log_solution.x)

log_total_capacity = (
    log_capacity_A * log_x
    + log_capacity_B * log_y
)

print("\nPART 3: CYBERSECURITY LOG PROCESSING")
print("Optimization success:", log_solution.success)
print(f"Type A resource allocation: {log_x:.3f}")
print(f"Type B resource allocation: {log_y:.3f}")
print(f"Total log processing capacity: {log_total_capacity:.2f}")
print(f"Minimum resource cost: {log_total_cost:.2f}")


# ==========================================
# PART 4: VISUALIZE OPTIMIZATION RESULTS
# ==========================================

labels = [
    "Original cloud",
    "Modified cloud",
    "Cybersecurity logs"
]

costs = [
    total_cost,
    modified_cost,
    log_total_cost
]

plt.figure(figsize=(9, 6))

plt.bar(labels, costs)

plt.xlabel("Optimization scenario")
plt.ylabel("Minimum operating cost")
plt.title("Comparison of Optimized Operating Costs")

plt.grid(axis="y")

plt.savefig(
    OUTPUT_DIR / "optimization_results.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
