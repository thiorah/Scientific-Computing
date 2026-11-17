
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline
import os

# Create output folder if it does not exist
os.makedirs("task_13_interpolation/output", exist_ok=True)

# -------------------------------------------------
# PART 1: ORIGINAL HOURLY TEMPERATURE MEASUREMENTS
# -------------------------------------------------

hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)

temperature = np.array(
    [18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0]
)

# Create interpolation functions
linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

# Generate estimates every 10 minutes
ten_minute_times = np.arange(8, 14 + 1/6, 1/6)

linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)

# Estimate temperature at 10:30 AM
target_time = 10.5

print("PART 1: ORIGINAL TEMPERATURE DATA")
print("---------------------------------")
print(f"Linear estimate at 10:30: {float(linear(target_time)):.2f} C")
print(f"Cubic estimate at 10:30: {float(cubic(target_time)):.2f} C")


# -------------------------------------------------
# PART 2: MODIFY ONE INPUT MEASUREMENT
# -------------------------------------------------

modified_temperature = temperature.copy()

# Change the 11:00 AM reading from 24 to 26 degrees
modified_temperature[3] = 26.0

modified_linear = interp1d(
    hours, modified_temperature, kind="linear"
)

modified_cubic = CubicSpline(
    hours, modified_temperature
)

print("\nPART 2: MODIFIED TEMPERATURE DATA")
print("---------------------------------")
print(
    f"New linear estimate at 10:30: "
    f"{float(modified_linear(target_time)):.2f} C"
)
print(
    f"New cubic estimate at 10:30: "
    f"{float(modified_cubic(target_time)):.2f} C"
)


# -------------------------------------------------
# PART 3: NEW REAL-WORLD APPLICATION
# GREENHOUSE HUMIDITY SENSOR
# -------------------------------------------------

# Humidity readings recorded hourly
humidity = np.array(
    [60.0, 63.0, 67.0, 72.0, 75.0, 73.0, 70.0]
)

humidity_linear = interp1d(
    hours, humidity, kind="linear"
)

humidity_cubic = CubicSpline(
    hours, humidity
)

humidity_time = 11.5

print("\nPART 3: GREENHOUSE HUMIDITY APPLICATION")
print("---------------------------------------")
print(
    f"Estimated humidity at 11:30 using linear: "
    f"{float(humidity_linear(humidity_time)):.2f}%"
)
print(
    f"Estimated humidity at 11:30 using cubic: "
    f"{float(humidity_cubic(humidity_time)):.2f}%"
)


# -------------------------------------------------
# PART 4: PLOT THE RESULTS
# -------------------------------------------------

fig, axes = plt.subplots(2, 1, figsize=(10, 9))

# Original and modified temperature
axes[0].scatter(
    hours, temperature,
    label="Original measurements"
)

axes[0].plot(
    ten_minute_times, linear_estimates,
    label="Linear interpolation"
)

axes[0].plot(
    ten_minute_times, cubic_estimates,
    label="Cubic spline interpolation"
)

axes[0].plot(
    hours, modified_temperature,
    marker="o", linestyle="--",
    label="Modified measurements"
)

axes[0].set_title("Temperature Interpolation")
axes[0].set_xlabel("Time (hour)")
axes[0].set_ylabel("Temperature (C)")
axes[0].legend()
axes[0].grid(True)

# Greenhouse humidity
axes[1].scatter(
    hours, humidity,
    label="Hourly humidity measurements"
)

axes[1].plot(
    ten_minute_times,
    humidity_linear(ten_minute_times),
    label="Linear interpolation"
)

axes[1].plot(
    ten_minute_times,
    humidity_cubic(ten_minute_times),
    label="Cubic spline interpolation"
)

axes[1].set_title("Greenhouse Humidity Interpolation")
axes[1].set_xlabel("Time (hour)")
axes[1].set_ylabel("Humidity (%)")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()

plt.savefig(
    "task_13_interpolation/output/temperature_interpolation.png"
)

plt.show()

print("\nGraph saved successfully.")
