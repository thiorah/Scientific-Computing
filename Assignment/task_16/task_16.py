
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson, trapezoid

# ==================================================
# PART 1: ORIGINAL SMART-METER ENERGY CALCULATION
# ==================================================

# Time readings in hours (every 2 hours)
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)

# Power readings in kilowatts
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])

# Calculate total energy using two methods
energy_trapezoid = trapezoid(power_kw, x=time_hours)
energy_simpson = simpson(power_kw, x=time_hours)

print("PART 1: ORIGINAL SMART-METER RESULTS")
print(f"Energy using Trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule: {energy_simpson:.3f} kWh")
print(
    "Difference between estimates:",
    f"{abs(energy_simpson - energy_trapezoid):.3f} kWh"
)


# ==================================================
# PART 2: MODIFY ONE POWER READING
# ==================================================

# Change the power reading at 6 hours from 1.8 kW to 2.2 kW
modified_power = power_kw.copy()
modified_power[3] = 2.2

modified_trapezoid = trapezoid(
    modified_power, x=time_hours
)

modified_simpson = simpson(
    modified_power, x=time_hours
)

print("\nPART 2: MODIFIED SMART-METER RESULTS")
print(f"Modified energy using Trapezoidal rule: {modified_trapezoid:.3f} kWh")
print(f"Modified energy using Simpson's rule: {modified_simpson:.3f} kWh")


# ==================================================
# PART 3: NEW APPLICATION - WATER FLOW MONITORING
# ==================================================

# Simulated water flow readings in litres per minute
water_flow = np.array([12, 14, 18, 20, 17, 15, 11], dtype=float)

# Time is measured in minutes for this new application
time_minutes = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)

# Calculate total water volume in litres
water_trapezoid = trapezoid(
    water_flow, x=time_minutes
)

water_simpson = simpson(
    water_flow, x=time_minutes
)

print("\nPART 3: WATER FLOW MONITORING")
print(f"Total water using Trapezoidal rule: {water_trapezoid:.3f} litres")
print(f"Total water using Simpson's rule: {water_simpson:.3f} litres")


# ==================================================
# PART 4: VISUALIZE THE RESULTS
# ==================================================

fig, axes = plt.subplots(2, 1, figsize=(10, 9))

# Original and modified power readings
axes[0].plot(
    time_hours,
    power_kw,
    marker="o",
    label="Original power"
)

axes[0].plot(
    time_hours,
    modified_power,
    marker="s",
    linestyle="--",
    label="Modified power"
)

axes[0].set_title("Smart-Meter Power Readings")
axes[0].set_xlabel("Time (hours)")
axes[0].set_ylabel("Power (kW)")
axes[0].legend()
axes[0].grid(True)

# Water flow readings
axes[1].plot(
    time_minutes,
    water_flow,
    marker="o",
    label="Water flow"
)

axes[1].set_title("Water Flow Rate Over Time")
axes[1].set_xlabel("Time (minutes)")
axes[1].set_ylabel("Flow rate (litres/minute)")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()

# Save the graph
plt.savefig(
    "task_16_numerical_integration/output/integration_results.png"
)

plt.show()
