# Task 02: NumPy Arrays and Numerical Computation

## 1. Objective

To use NumPy arrays to store numerical readings and perform statistical calculations on IoT sensor data.

## 2. Original Problem

An IoT temperature sensor records five readings. NumPy is used to calculate the average, maximum, minimum, range and standard deviation of the readings.

## 3. Input Data

Temperature readings: 24.5, 25.0, 26.2, 25.8 and 27.1 degrees Celsius.

## 4. Mathematical Operations

- Mean: sum of readings divided by the number of readings.
- Maximum: highest reading in the array.
- Minimum: lowest reading in the array.
- Range: maximum minus minimum.
- Standard deviation: measures the spread of readings around their mean.

## 5. Modified Input and Results

The final temperature reading was changed from 27.1°C to 30.0°C.

The average increased from 25.72°C to 26.30°C, while the range increased from 2.60°C to 5.50°C. This demonstrates how changing one input affects the statistical results.

## 6. Related Real-World Application

The program was modified to analyze network latency measurements of 42, 48, 45, 120 and 50 milliseconds.

The average latency was 61 milliseconds, and the maximum was 120 milliseconds. The higher reading increases the range and may warrant further investigation.

## 7. Assumptions

- The sensor readings are valid numerical measurements.
- The temperature measurements use the same unit.
- The network latency measurements use milliseconds.
- The five measurements are sufficient for demonstrating the calculations, but not for making a definitive assessment of sensor or network performance.

## 8. Conclusion

NumPy simplifies numerical calculations by allowing multiple readings to be processed efficiently. Changing an input demonstrated how statistical results respond to changes in data. The same operations can be applied to temperature monitoring and network performance analysis.