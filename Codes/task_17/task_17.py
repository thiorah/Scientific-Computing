
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# TASK 17: ORDINARY DIFFERENTIAL EQUATIONS
# EULER'S METHOD
# ==========================================

# PART 1: ORIGINAL COOLING PROBLEM

T_ambient = 25.0
T_initial = 90.0
k = 0.12

h = 1.0
end_time = 30.0


# Newton's law of cooling
def cooling_rate(T):
    return -k * (T - T_ambient)


# Generate time values
time = np.arange(0, end_time + h, h)

# Store temperature values
temperature = np.zeros_like(time)
temperature[0] = T_initial

# Apply Euler's method
for i in range(len(time) - 1):
    temperature[i + 1] = (
        temperature[i] + h * cooling_rate(temperature[i])
    )

# Exact solution for comparison
exact = T_ambient + (T_initial - T_ambient) * np.exp(-k * time)

print("PART 1: ORIGINAL COOLING PROBLEM")
print(f"Euler temperature after 30 min: {temperature[-1]:.2f} C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} C")
print(f"Final absolute error: {abs(temperature[-1] - exact[-1]):.4f} C")


# PART 2: CHANGE THE TIME STEP

h_modified = 0.5

time_modified = np.arange(0, end_time + h_modified, h_modified)

temperature_modified = np.zeros_like(time_modified)
temperature_modified[0] = T_initial

for i in range(len(time_modified) - 1):
    temperature_modified[i + 1] = (
        temperature_modified[i]
        + h_modified * cooling_rate(temperature_modified[i])
    )

print("\nPART 2: MODIFIED TIME STEP")
print(f"New time step: {h_modified} minutes")
print(f"Euler temperature after 30 min: {temperature_modified[-1]:.2f} C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} C")
print(
    "Final absolute error:",
    f"{abs(temperature_modified[-1] - exact[-1]):.4f} C"
)


# PART 3: NEW APPLICATION - BATTERY DISCHARGING

# A battery starts at 5 volts and gradually loses voltage.
V_initial = 5.0
decay_constant = 0.08
battery_step = 0.5
battery_end_time = 10.0

def battery_rate(V):
    return -decay_constant * V

battery_time = np.arange(
    0, battery_end_time + battery_step, battery_step
)

voltage = np.zeros_like(battery_time)
voltage[0] = V_initial

for i in range(len(battery_time) - 1):
    voltage[i + 1] = (
        voltage[i] + battery_step * battery_rate(voltage[i])
    )

# Exact battery discharge solution for comparison
exact_voltage = V_initial * np.exp(
    -decay_constant * battery_time
)

print("\nPART 3: BATTERY DISCHARGING APPLICATION")
print(f"Initial battery voltage: {V_initial:.2f} V")
print(f"Voltage after 10 hours: {voltage[-1]:.2f} V")
print(f"Exact voltage after 10 hours: {exact_voltage[-1]:.2f} V")


# PART 4: PLOT THE RESULTS

plt.figure(figsize=(10, 6))

plt.plot(
    time,
    temperature,
    marker="o",
    markersize=3,
    label="Euler (1 minute)"
)

plt.plot(
    time_modified,
    temperature_modified,
    label="Euler (0.5 minute)"
)

plt.plot(
    time,
    exact,
    linestyle="--",
    label="Exact solution"
)

plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Cooling of a Hot Object Using Euler's Method")
plt.legend()
plt.grid(True)

plt.savefig(
    "task_17_euler_ode/output/cooling_results.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


plt.figure(figsize=(10, 6))

plt.plot(
    battery_time,
    voltage,
    marker="o",
    markersize=3,
    label="Euler estimate"
)

plt.plot(
    battery_time,
    exact_voltage,
    linestyle="--",
    label="Exact solution"
)

plt.xlabel("Time (hours)")
plt.ylabel("Battery voltage (V)")
plt.title("Battery Voltage Discharge Using Euler's Method")
plt.legend()
plt.grid(True)

plt.savefig(
    "task_17_euler_ode/output/battery_discharge.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
