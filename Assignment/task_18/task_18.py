
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from pathlib import Path

# ==========================================
# TASK 18: NUMERICAL SOLUTION OF ODEs
# USING SCIPY solve_ivp
# ==========================================

# Automatically create output folder
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ==========================================
# PART 1: ORIGINAL RC CHARGING CIRCUIT
# ==========================================

Vs = 5.0       # Supply voltage (V)
R = 1000.0     # Resistance (ohms)
C = 0.001      # Capacitance (farads)
V0 = 0.0       # Initial capacitor voltage

# RC circuit differential equation
def rc_circuit(t, V):
    return [(Vs - V[0]) / (R * C)]


# Time values for displaying the solution
t_eval = np.linspace(0, 5, 200)

# Solve the differential equation
solution = solve_ivp(
    rc_circuit,
    (0, 5),
    [V0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

# Exact mathematical solution for comparison
exact = Vs * (1 - np.exp(-solution.t / (R * C)))

# Display original results
print("PART 1: ORIGINAL RC CIRCUIT")
print("Solver success:", solution.success)

print(
    f"Capacitor voltage at 5 seconds: "
    f"{solution.y[0, -1]:.4f} V"
)

print(
    f"Exact voltage at 5 seconds: "
    f"{exact[-1]:.4f} V"
)

print(
    "Maximum error against exact solution:",
    f"{np.max(np.abs(solution.y[0] - exact)):.3e} V"
)


# ==========================================
# PART 2: MODIFY CAPACITANCE
# ==========================================

C_modified = 0.002  # Increase capacitance from 0.001 F

def modified_rc_circuit(t, V):
    return [(Vs - V[0]) / (R * C_modified)]


modified_solution = solve_ivp(
    modified_rc_circuit,
    (0, 5),
    [V0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

modified_exact = Vs * (
    1 - np.exp(-modified_solution.t / (R * C_modified))
)

print("\nPART 2: MODIFIED RC CIRCUIT")
print(f"New capacitance: {C_modified} F")

print(
    f"Capacitor voltage at 5 seconds: "
    f"{modified_solution.y[0, -1]:.4f} V"
)

print(
    f"Exact voltage at 5 seconds: "
    f"{modified_exact[-1]:.4f} V"
)


# ==========================================
# PART 3: CYBERSECURITY APPLICATION
# SIMULATING MALWARE INFECTION SPREAD
# ==========================================

# Simplified model of infection spreading
# across a network of connected devices.

initial_infected = 5
growth_rate = 0.25
maximum_devices = 1000

def malware_spread(t, I):
    return [
        growth_rate * I[0] *
        (1 - I[0] / maximum_devices)
    ]


cyber_time = np.linspace(0, 24, 200)

cyber_solution = solve_ivp(
    malware_spread,
    (0, 24),
    [initial_infected],
    t_eval=cyber_time,
    rtol=1e-9,
    atol=1e-11
)

print("\nPART 3: MALWARE SPREAD SIMULATION")
print(f"Initial infected devices: {initial_infected}")
print(f"Maximum network devices: {maximum_devices}")

print(
    f"Estimated infected devices after 24 hours: "
    f"{cyber_solution.y[0, -1]:.2f}"
)


# ==========================================
# PART 4: PLOT ORIGINAL AND MODIFIED CIRCUIT
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    solution.t,
    solution.y[0],
    label="Original RC circuit",
)

plt.plot(
    modified_solution.t,
    modified_solution.y[0],
    label="Modified RC circuit",
)

plt.plot(
    solution.t,
    exact,
    linestyle="--",
    label="Original exact solution"
)

plt.xlabel("Time (seconds)")
plt.ylabel("Capacitor voltage (V)")
plt.title("RC Circuit Charging Using solve_ivp")
plt.legend()
plt.grid(True)

plt.savefig(
    OUTPUT_DIR / "rc_circuit_results.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# PART 5: PLOT CYBERSECURITY APPLICATION
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    cyber_solution.t,
    cyber_solution.y[0],
    label="Estimated infected devices"
)

plt.xlabel("Time (hours)")
plt.ylabel("Number of infected devices")
plt.title("Simulated Malware Spread in a Network")
plt.legend()
plt.grid(True)

plt.savefig(
    OUTPUT_DIR / "malware_spread.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
