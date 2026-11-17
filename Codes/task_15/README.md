# Task 15: Numerical Differentiation

## 1. Objective
To estimate the rate of change of a quantity using numerical differentiation. The program estimates vehicle speed from GPS position measurements and applies the same method to network data transfer rates.

## 2. Mathematical Concept
Numerical differentiation approximates derivatives using nearby measurements.

- Forward difference: uses the current and next values.
- Central difference: uses the previous and next values.
- Backward difference: uses the current and previous values.

Central differences are often more accurate for interior measurements.

## 3. Input Data
The original program uses GPS position measurements recorded every second:

- Time: 0 to 6 seconds.
- Position: 0, 4.8, 10.2, 16.1, 22.7, 30.0 and 38.0 metres.

## 4. Tools Used
- Python
- NumPy for numerical calculations.
- Matplotlib for plotting results.

## 5. Original Results
The estimated vehicle speed increases from 4.80 m/s at the beginning to 8.00 m/s at the end. This indicates that the vehicle is increasing its speed over time.

## 6. Modified Experiment
The GPS position at 5 seconds was changed from 30 metres to 33 metres.

This affected the estimated speeds at nearby measurement points. It demonstrates how changes in recorded data influence numerical derivative calculations.

## 7. New Real-World Application
The method was applied to network monitoring. Simulated server data measurements were used to estimate the rate of data transfer in megabytes per second.

This can help identify changes in network traffic and monitor server performance.

## 8. Conclusion
Numerical differentiation is useful for estimating rates of change when continuous mathematical formulas are unavailable. It can be applied in GPS tracking, vehicle speed estimation, network monitoring and sensor analysis.