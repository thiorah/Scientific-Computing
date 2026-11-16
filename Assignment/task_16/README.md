# Task 16: Numerical Integration

## 1. Objective
To calculate accumulated quantities from measurements recorded over time using numerical integration.

## 2. Mathematical Concept
Numerical integration estimates the area under a curve.

Two methods are used:

- Trapezoidal rule: estimates the area using trapezoids.
- Simpson's rule: estimates the area using parabolic sections.

## 3. Input Data
The original example uses smart-meter power readings taken every two hours.

Time (hours): 0, 2, 4, 6, 8, 10, 12.

Power (kW): 0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9.

## 4. Tools Used
- Python
- NumPy for numerical arrays.
- SciPy for numerical integration.
- Matplotlib for visualization.

## 5. Original Results
- Trapezoidal rule: 15.700 kWh.
- Simpson's rule: 15.800 kWh.
- Difference: 0.100 kWh.

Both methods estimate approximately the same energy consumption.

## 6. Modified Experiment
The power reading at 6 hours was increased from 1.8 kW to 2.2 kW.

The estimated energy increased to:
- Trapezoidal rule: 16.500 kWh.
- Simpson's rule: 16.867 kWh.

This demonstrates how an increase in power consumption affects total energy usage.

## 7. New Real-World Application
Numerical integration was applied to water-flow monitoring. Simulated flow readings were used to estimate the total volume of water passing through a pipe over 12 minutes.

Results:
- Trapezoidal rule: 191.000 litres.
- Simpson's rule: 192.667 litres.

This method can support water usage monitoring, irrigation and water distribution systems.

## 8. Conclusion
Numerical integration is useful for estimating accumulated quantities when measurements change over time. It can be applied to electricity consumption, water flow, distance calculations and other engineering problems.