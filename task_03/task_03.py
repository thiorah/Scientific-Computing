
import numpy as np
import timeit


def python_loop(traffic_values):
    """Convert traffic from MB/minute to Mbps using a loop."""
    results = []

    for value in traffic_values:
        results.append(value * 8 / 60)

    return results


def numpy_vectorized(traffic_values):
    """Convert traffic from MB/minute to Mbps using NumPy."""
    return traffic_values * 8 / 60


# PART 1: Original network traffic measurements
# Each value represents megabytes transferred per minute.
traffic = np.array([12, 18, 25, 20, 35], dtype=float)

loop_results = python_loop(traffic)
vectorized_results = numpy_vectorized(traffic)

print("TASK 03: MATHEMATICAL FUNCTIONS AND VECTORIZATION")
print("\nOriginal traffic (MB/min):", traffic)
print("\nLoop results (Mbps):", np.round(loop_results, 2))
print("NumPy results (Mbps):", np.round(vectorized_results, 2))

# Verify that both methods give the same numerical results.
print(
    "\nDo both methods agree?",
    np.allclose(loop_results, vectorized_results)
)


# PART 2: Modify one input
modified_traffic = traffic.copy()
modified_traffic[4] = 50

modified_results = numpy_vectorized(modified_traffic)

print("\nModified traffic (MB/min):", modified_traffic)
print("Modified rates (Mbps):", np.round(modified_results, 2))
print(f"Original mean rate: {np.mean(vectorized_results):.2f} Mbps")
print(f"Modified mean rate: {np.mean(modified_results):.2f} Mbps")


# PART 3: Compare processing speed on a larger dataset
large_traffic = np.linspace(1, 100000, 100000)

loop_time = timeit.timeit(
    lambda: python_loop(large_traffic),
    number=10
)

numpy_time = timeit.timeit(
    lambda: numpy_vectorized(large_traffic),
    number=10
)

print("\nPERFORMANCE COMPARISON")
print("Dataset size:", len(large_traffic))
print(f"Python loop time for 10 runs: {loop_time:.6f} seconds")
print(f"NumPy vectorized time for 10 runs: {numpy_time:.6f} seconds")

if numpy_time > 0:
    print(f"Speed-up: {loop_time / numpy_time:.2f}x")
