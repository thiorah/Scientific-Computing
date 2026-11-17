# Task 14: Curve Fitting and Approximation

## 1. Objective
To use Python and numerical methods to fit a mathematical curve to observed data, analyse the relationship between variables and predict future values.

## 2. Mathematical Concept
Curve fitting finds a mathematical equation that best represents observed data.

This task uses a quadratic model:

**y = ax² + bx + c**

Where x represents the number of users, y represents response time, and a, b and c are calculated parameters.

## 3. Input Data
The original dataset contains concurrent server users and their measured response times:

| Users | Response Time (ms) |
|---:|---:|
| 50 | 82 |
| 100 | 95 |
| 150 | 115 |
| 200 | 145 |
| 250 | 185 |
| 300 | 238 |
| 350 | 305 |

## 4. Tools and Libraries
- Python
- NumPy
- SciPy (`curve_fit`)
- Matplotlib

## 5. Original Results
- Fitted equation: y = 0.002167x² - 0.1345x + 85.00
- RMSE: approximately 1.55 ms.
- Predicted response time at 400 users: approximately 377.86 ms.

## 6. Modified Experiment
The response time at 350 users was changed from 305 ms to 340 ms.

The new prediction at 400 users increased to approximately 422.86 ms. The RMSE also increased to approximately 7.79 ms.

## 7. New Real-World Application
The program was modified to analyse network latency as the number of connected devices increases. Using illustrative network measurements, the model predicted a latency of approximately 130 ms at 160 devices.

## 8. Interpretation
The results show that response time and network latency increase as the number of users or devices increases. Curve fitting provides a mathematical way to understand these relationships and estimate values.

## 9. Conclusion
Curve fitting is useful in server performance analysis, network monitoring, forecasting and data analysis. The accuracy of predictions depends on the quality of the data and the suitability of the mathematical model.