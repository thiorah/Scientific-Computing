# Task 03: Mathematical Functions and Vectorization

## 1. Objective

To apply mathematical operations to network traffic measurements and compare Python loops with NumPy vectorization.

## 2. Original Problem

Network traffic measurements are recorded in megabytes per minute. The program converts these measurements into megabits per second using two approaches: a Python loop and a NumPy vectorized operation.

## 3. Input Data

Original traffic measurements: 12, 18, 25, 20 and 35 MB/minute.

## 4. Mathematical Operation

Rate in Mbps = (Traffic in MB/minute × 8) / 60.

The factor of 8 converts bytes to bits, and division by 60 converts minutes to seconds.

## 5. Results and Comparison

Both approaches should produce equivalent numerical results. The original mean rate is approximately 2.93 Mbps.

The program also measures execution time over 100,000 values for ten runs. The measured times are used to compare the performance of the two methods.

## 6. Modified Input

The final traffic measurement was increased from 35 to 50 MB/minute.

The mean rate increased from approximately 2.93 Mbps to 3.60 Mbps. The modified final rate became approximately 6.67 Mbps.

## 7. Related Real-World Application

The method can be used to convert large sets of network traffic measurements into consistent units for network monitoring and performance analysis.

## 8. Assumptions

- Traffic values represent megabytes transferred per minute.
- One megabyte is treated as eight megabits for this calculation.
- All measurements use consistent units.
- The timing experiment uses the same dataset and number of runs for both methods.

## 9. Conclusion

Python loops and NumPy vectorization can perform the same mathematical conversion. Vectorization provides a concise approach that often improves performance on large numerical datasets. Changing an input demonstrated how the calculated traffic rate and mean respond to changes in the measurements.