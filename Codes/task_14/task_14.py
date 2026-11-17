
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

# Create output folder
os.makedirs("task_14_curve_fitting/output", exist_ok=True)


# -------------------------------------------------
# PART 1: ORIGINAL SERVER RESPONSE-TIME DATA
# -------------------------------------------------

# Number of concurrent users
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)

# Measured response time in milliseconds
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)


# Define a quadratic model
def model(x, a, b, c):
    return a * x**2 + b * x + c


# Fit the model to the observed data
parameters, covariance = curve_fit(model, users, response_ms)

a, b, c = parameters

# Calculate predicted values for the original measurements
predicted = model(users, a, b, c)

# Calculate Root Mean Square Error (RMSE)
rmse = np.sqrt(np.mean((response_ms - predicted)**2))

# Predict response time at 400 users
prediction_400 = model(400, a, b, c)

print("PART 1: ORIGINAL SERVER DATA")
print("--------------------------------")
print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 400 users: {prediction_400:.2f} ms")


# -------------------------------------------------
# PART 2: MODIFY ONE INPUT MEASUREMENT
# -------------------------------------------------

modified_response = response_ms.copy()

# Change response time at 350 users from 305 ms to 340 ms
modified_response[-1] = 340

modified_parameters, modified_covariance = curve_fit(
    model, users, modified_response
)

ma, mb, mc = modified_parameters

modified_predicted = model(users, ma, mb, mc)

modified_rmse = np.sqrt(
    np.mean((modified_response - modified_predicted)**2)
)

modified_400 = model(400, ma, mb, mc)

print("\nPART 2: MODIFIED SERVER DATA")
print("--------------------------------")
print(f"New fitted model: y = {ma:.6f}x^2 + {mb:.4f}x + {mc:.2f}")
print(f"New RMSE: {modified_rmse:.2f} ms")
print(f"New prediction at 400 users: {modified_400:.2f} ms")


# -------------------------------------------------
# PART 3: NEW REAL-WORLD APPLICATION
# NETWORK LATENCY AND CONNECTED DEVICES
# -------------------------------------------------

# Illustrative measurements of network latency
devices = np.array([20, 40, 60, 80, 100, 120, 140], dtype=float)

latency_ms = np.array([18, 22, 30, 42, 58, 78, 102], dtype=float)

# Fit the quadratic model
network_parameters, network_covariance = curve_fit(
    model, devices, latency_ms
)

na, nb, nc = network_parameters

network_predicted = model(devices, na, nb, nc)

network_rmse = np.sqrt(
    np.mean((latency_ms - network_predicted)**2)
)

# Estimate latency at 160 connected devices
latency_160 = model(160, na, nb, nc)

print("\nPART 3: NETWORK LATENCY APPLICATION")
print("--------------------------------")
print(f"Fitted model: y = {na:.6f}x^2 + {nb:.4f}x + {nc:.2f}")
print(f"RMSE: {network_rmse:.2f} ms")
print(f"Predicted latency at 160 devices: {latency_160:.2f} ms")


# -------------------------------------------------
# PART 4: PLOT THE RESULTS
# -------------------------------------------------

fig, axes = plt.subplots(3, 1, figsize=(10, 14))

# Original server response-time curve
x_plot = np.linspace(50, 400, 300)

axes[0].scatter(
    users, response_ms,
    label="Measured response time"
)

axes[0].plot(
    x_plot, model(x_plot, a, b, c),
    label="Fitted quadratic curve"
)

axes[0].set_title("Original Server Response Time")
axes[0].set_xlabel("Concurrent users")
axes[0].set_ylabel("Response time (ms)")
axes[0].legend()
axes[0].grid(True)


# Modified server response-time curve
axes[1].scatter(
    users, modified_response,
    label="Modified measurements"
)

axes[1].plot(
    x_plot, model(x_plot, ma, mb, mc),
    label="Modified fitted curve"
)

axes[1].set_title("Modified Server Response Time")
axes[1].set_xlabel("Concurrent users")
axes[1].set_ylabel("Response time (ms)")
axes[1].legend()
axes[1].grid(True)


# Network latency curve
network_plot = np.linspace(20, 160, 300)

axes[2].scatter(
    devices, latency_ms,
    label="Measured network latency"
)

axes[2].plot(
    network_plot,
    model(network_plot, na, nb, nc),
    label="Fitted latency curve"
)

axes[2].set_title("Network Latency vs Connected Devices")
axes[2].set_xlabel("Connected devices")
axes[2].set_ylabel("Latency (ms)")
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()

plt.savefig(
    "task_14_curve_fitting/output/server_curve_fitting.png"
)

plt.show()

print("\nGraph saved successfully.")
