
import numpy as np


def analyze_readings(title, readings, unit):
    """Calculate and display statistics for a set of readings."""

    readings = np.array(readings, dtype=float)

    print(f"\n--- {title} ---")
    print("Readings:", readings)
    print("Number of readings:", len(readings))
    print(f"Average: {np.mean(readings):.2f} {unit}")
    print(f"Maximum: {np.max(readings):.2f} {unit}")
    print(f"Minimum: {np.min(readings):.2f} {unit}")
    print(f"Range: {np.ptp(readings):.2f} {unit}")
    print(f"Standard deviation: {np.std(readings):.2f} {unit}")


# PART 1: Original IoT temperature sensor readings
temperature_readings = [24.5, 25.0, 26.2, 25.8, 27.1]

analyze_readings(
    "Original Temperature Readings",
    temperature_readings,
    "degrees C"
)


# PART 2: Change one input and observe the effect
modified_readings = [24.5, 25.0, 26.2, 25.8, 30.0]

analyze_readings(
    "Modified Temperature Readings",
    modified_readings,
    "degrees C"
)


# PART 3: Apply the same numerical method to network latency
network_latency = [42, 48, 45, 120, 50]

analyze_readings(
    "Network Latency Analysis",
    network_latency,
    "milliseconds"
)
