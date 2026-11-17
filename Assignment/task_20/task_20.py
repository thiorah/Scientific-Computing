
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# TASK 20: RANDOM NUMBERS AND MONTE CARLO
# METHODS
# ==========================================

# Automatically create output folder
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Reproducible random number generator
rng = np.random.default_rng(42)


# ==========================================
# PART 1: ORIGINAL SERVER OVERLOAD PROBLEM
# ==========================================

capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

# Generate random demand scenarios
demand = rng.normal(mean_demand, std_demand, N)

# Identify overloaded scenarios
overloaded = demand > capacity

# Estimate overload probability
overload_probability = overloaded.mean()

print("PART 1: ORIGINAL SERVER OVERLOAD SIMULATION")
print(f"Server capacity: {capacity:.0f}")
print(f"Average demand: {mean_demand:.0f}")
print(f"Demand standard deviation: {std_demand:.0f}")
print(f"Number of simulations: {N}")

print(
    f"Estimated overload probability: "
    f"{overload_probability:.4%}"
)

print(
    f"Number of overload cases: "
    f"{overloaded.sum()} out of {N}"
)


# Calculate running probability
running_probability = (
    np.cumsum(overloaded) / np.arange(1, N + 1)
)


# ==========================================
# PART 2: MODIFY SERVER CAPACITY
# ==========================================

# Increase server capacity from 1000 to 1100
modified_capacity = 1100.0

modified_overloaded = demand > modified_capacity

modified_probability = modified_overloaded.mean()

print("\nPART 2: MODIFIED SERVER CAPACITY")
print(f"New server capacity: {modified_capacity:.0f}")

print(
    f"New estimated overload probability: "
    f"{modified_probability:.4%}"
)

print(
    f"Number of overload cases: "
    f"{modified_overloaded.sum()} out of {N}"
)


# ==========================================
# PART 3: CYBERSECURITY APPLICATION
# SIMULATING SUCCESSFUL ATTACK ATTEMPTS
# ==========================================

# Simulate 100,000 security monitoring periods.
# Each period has 100 suspicious attack attempts.
# Assume each attempt has a 2% chance of success.

monitoring_periods = 100_000
attempts_per_period = 100
success_probability = 0.02

successful_attacks = rng.binomial(
    attempts_per_period,
    success_probability,
    monitoring_periods
)

# Define a high-risk period as 5 or more successful attempts
high_risk_periods = successful_attacks >= 5

high_risk_probability = high_risk_periods.mean()

print("\nPART 3: CYBERSECURITY ATTACK SIMULATION")
print(f"Monitoring periods: {monitoring_periods}")
print(f"Attempts per period: {attempts_per_period}")
print(f"Success probability per attempt: {success_probability:.2%}")

print(
    f"Estimated high-risk period probability: "
    f"{high_risk_probability:.4%}"
)

print(
    f"High-risk periods: "
    f"{high_risk_periods.sum()} out of {monitoring_periods}"
)


# ==========================================
# PART 4: PLOT RUNNING OVERLOAD PROBABILITY
# ==========================================

indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

plt.figure(figsize=(10, 6))

plt.semilogx(
    indices + 1,
    running_probability[indices],
    label="Estimated overload probability"
)

plt.axhline(
    overload_probability,
    linestyle="--",
    label="Final estimated probability"
)

plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo Estimate of Server Overload Risk")
plt.legend()
plt.grid(True)

plt.savefig(
    OUTPUT_DIR / "overload_probability.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# PART 5: PLOT DEMAND DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

plt.hist(
    demand,
    bins=50,
    edgecolor="black"
)

plt.axvline(
    capacity,
    linestyle="--",
    label="Original server capacity"
)

plt.axvline(
    modified_capacity,
    linestyle=":",
    label="Modified server capacity"
)

plt.xlabel("Incoming server demand")
plt.ylabel("Frequency")
plt.title("Simulated Distribution of Server Demand")
plt.legend()
plt.grid(True)

plt.savefig(
    OUTPUT_DIR / "server_demand_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# PART 6: PLOT CYBERSECURITY RESULTS
# ==========================================

plt.figure(figsize=(10, 6))

plt.hist(
    successful_attacks,
    bins=np.arange(-0.5, attempts_per_period + 1.5, 1),
    edgecolor="black"
)

plt.axvline(
    5,
    linestyle="--",
    label="High-risk threshold"
)

plt.xlabel("Successful attack attempts per period")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulation of Security Attack Attempts")
plt.legend()
plt.grid(True)

plt.savefig(
    OUTPUT_DIR / "cybersecurity_attack_simulation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
