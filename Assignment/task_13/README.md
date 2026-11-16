# Task 13: Interpolation

## 1. Objective
To understand interpolation and use Python to estimate values between known data points using linear interpolation and cubic spline interpolation.

## 2. Mathematical Concept
Interpolation is a numerical method used to estimate unknown values between known measurements.

- Linear interpolation uses straight lines between neighbouring points.
- Cubic spline interpolation uses smooth cubic curves between data points.

## 3. Input Data
Hourly temperature measurements:

| Time | Temperature |
|---|---:|
| 8:00 | 18°C |
| 9:00 | 20°C |
| 10:00 | 22.5°C |
| 11:00 | 24°C |
| 12:00 | 25°C |
| 13:00 | 25.5°C |
| 14:00 | 25°C |

## 4. Tools and Libraries
- Python
- NumPy
- SciPy (`interp1d`, `CubicSpline`)
- Matplotlib

## 5. Results
At 10:30 AM:
- Linear interpolation estimated 23.25°C.
- Cubic spline interpolation estimated 23.36°C.

After changing the 11:00 AM measurement from 24°C to 26°C:
- Linear estimate increased to 24.25°C.
- Cubic estimate increased to 24.58°C.

## 6. New Real-World Application
The program was modified to estimate humidity levels in a greenhouse using hourly sensor readings. At 11:30 AM, linear interpolation estimated 73.50% humidity, while cubic spline estimated 74.03%.

## 7. Interpretation
Both methods successfully estimate values between recorded measurements. Cubic spline produces a smoother curve, while linear interpolation is simpler. Changing the input measurements affects the estimated results.

## 8. Conclusion
Interpolation is useful in sensor monitoring, scientific experiments and data analysis because it helps estimate missing values between recorded measurements.