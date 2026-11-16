
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
import os

print("TASK 11: NEWTON-RAPHSON AND SECANT METHODS")


# PART 1: Original investment cash flows
cash_flows = [-10000, 3000, 3500, 4000, 2500]


# PART 2: Define the Net Present Value function
def npv(rate, flows):
    return sum(
        cf / (1 + rate) ** t
        for t, cf in enumerate(flows)
    )


# PART 3: Define the derivative of NPV
def d_npv(rate, flows):
    return sum(
        -t * cf / (1 + rate) ** (t + 1)
        for t, cf in enumerate(flows)
        if t > 0
    )


# Function to calculate IRR using both methods
def calculate_irr(flows, title):

    newton = root_scalar(
        lambda r: npv(r, flows),
        fprime=lambda r: d_npv(r, flows),
        x0=0.10,
        method="newton",
        xtol=1e-12
    )

    secant = root_scalar(
        lambda r: npv(r, flows),
        x0=0.05,
        x1=0.20,
        method="secant",
        xtol=1e-12
    )

    print(f"\n--- {title} ---")
    print(f"Newton-Raphson IRR: {newton.root:.6%}")
    print(f"Secant IRR: {secant.root:.6%}")

    print("Newton iterations:", newton.iterations)
    print("Secant iterations:", secant.iterations)

    print(
        "NPV at Newton solution:",
        f"{npv(newton.root, flows):.8f}"
    )

    print(
        "NPV at Secant solution:",
        f"{npv(secant.root, flows):.8f}"
    )

    return newton.root, secant.root


# PART 4: Solve the original investment
original_newton, original_secant = calculate_irr(
    cash_flows,
    "ORIGINAL INVESTMENT"
)


# PART 5: Modify one cash flow
# Increase Year 3 cash inflow from 4000 to 5000.

modified_flows = [-10000, 3000, 3500, 5000, 2500]

modified_newton, modified_secant = calculate_irr(
    modified_flows,
    "MODIFIED INVESTMENT"
)


# PART 6: New real-world application
# Analyse a different investment project.

project_flows = [-15000, 4000, 5000, 6000, 7000]

project_newton, project_secant = calculate_irr(
    project_flows,
    "NEW BUSINESS PROJECT"
)


# PART 7: Plot the original NPV function
rates = np.linspace(0.01, 0.50, 300)

npv_values = [
    npv(rate, cash_flows)
    for rate in rates
]

os.makedirs(
    "task_11_newton_secant/output",
    exist_ok=True
)

plt.figure(figsize=(9, 5))

plt.plot(rates * 100, npv_values, label="NPV")

plt.axhline(0, linewidth=0.8)
plt.axvline(
    original_newton * 100,
    linestyle="--",
    label="Calculated IRR"
)

plt.xlabel("Interest rate (%)")
plt.ylabel("Net Present Value")
plt.title("NPV Against Interest Rate")
plt.legend()
plt.grid(True)

plt.savefig(
    "task_11_newton_secant/output/npv_graph.png"
)

plt.show()

print("\nGraph saved successfully.")
print("Task 11 completed successfully.")
