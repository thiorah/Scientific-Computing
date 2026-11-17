
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# PART 1: ORIGINAL GPS SPEED ESTIMATION
# --------------------------------------------------

# Time in seconds
time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)

# GPS position measurements in metres
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])

# Create an array to store estimated speeds
speed = np.zeros_like(position)

# Forward difference at the first point
speed[0] = (position[1] - position[0]) / (time[1] - time[0])

# Central difference for the middle points
for i in range(1, len(time) - 1):
    speed[i] = (
        position[i + 1] - position[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference at the last point
speed[-1] = (
    position[-1] - position[-2]
) / (
    time[-1] - time[-2]
)

print("PART 1: ORIGINAL GPS SPEED ESTIMATES")

for t, x, v in zip(time, position, speed):
    print(
        f"Time: {t:.0f}s | "
        f"Position: {x:.1f}m | "
        f"Estimated speed: {v:.2f}m/s"
    )


# --------------------------------------------------
# PART 2: CHANGE ONE INPUT MEASUREMENT
# --------------------------------------------------

# Change the position recorded at 5 seconds
modified_position = position.copy()
modified_position[5] = 33.0

modified_speed = np.zeros_like(modified_position)

# Forward difference
modified_speed[0] = (
    modified_position[1] - modified_position[0]
) / (time[1] - time[0])

# Central differences
for i in range(1, len(time) - 1):
    modified_speed[i] = (
        modified_position[i + 1] - modified_position[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference
modified_speed[-1] = (
    modified_position[-1] - modified_position[-2]
) / (
    time[-1] - time[-2]
)

print("\nPART 2: MODIFIED GPS MEASUREMENTS")

for t, v in zip(time, modified_speed):
    print(f"Time: {t:.0f}s | Modified speed: {v:.2f}m/s")


# --------------------------------------------------
# PART 3: NEW APPLICATION - NETWORK TRAFFIC
# --------------------------------------------------

# Simulated data received by a server in megabytes
data_received = np.array(
    [0, 8, 19, 33, 50, 70, 93],
    dtype=float
)

# Estimate data transfer rate in MB/s
transfer_rate = np.zeros_like(data_received)

# Forward difference
transfer_rate[0] = (
    data_received[1] - data_received[0]
) / (time[1] - time[0])

# Central differences
for i in range(1, len(time) - 1):
    transfer_rate[i] = (
        data_received[i + 1] - data_received[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference
transfer_rate[-1] = (
    data_received[-1] - data_received[-2]
) / (
    time[-1] - time[-2]
)

print("\nPART 3: NETWORK DATA TRANSFER RATE")

for t, rate in zip(time, transfer_rate):
    print(f"Time: {t:.0f}s | Transfer rate: {rate:.2f} MB/s")


# --------------------------------------------------
# PART 4: PLOT THE RESULTS
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    time,
    speed,
    marker="o",
    label="Original GPS speed"
)

plt.plot(
    time,
    modified_speed,
    marker="s",
    linestyle="--",
    label="Modified GPS speed"
)

plt.xlabel("Time (seconds)")
plt.ylabel("Speed (m/s)")
plt.title("Vehicle Speed Estimated Using Numerical Differentiation")
plt.legend()
plt.grid(True)

# Save graph inside the output folder
plt.savefig(
    "task_15_numerical_differentiation/output/speed_estimation.png"
)

plt.show()
