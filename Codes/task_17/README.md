# Task 17: Ordinary Differential Equations – Euler Method

## 1. Objective
To use Euler's numerical method to estimate how a changing quantity behaves over time, using the cooling of a hot object as the main example.

## 2. Mathematical Concept
An Ordinary Differential Equation (ODE) describes how a quantity changes over time.

Euler's method uses:

**y(n+1) = y(n) + h × f(t, y)**

Where:
- y(n) is the current value.
- h is the time step.
- f(t, y) is the rate of change.

## 3. Original Problem
The program models the cooling of an object using Newton's Law of Cooling.

Input values:
- Ambient temperature: 25°C
- Initial temperature: 90°C
- Cooling constant: 0.12
- Time step: 1 minute
- Total time: 30 minutes

## 4. Tools Used
- Python
- NumPy
- Matplotlib
- VS Code

## 5. Original Results
Euler's method estimated the temperature after 30 minutes as approximately 26.40°C. The exact mathematical solution was approximately 26.78°C.

The object gradually cools towards the surrounding temperature.

## 6. Modified Experiment
The time step was changed from 1 minute to 0.5 minutes.

The new estimate was approximately 26.59°C, reducing the absolute error from 0.3720°C to 0.1890°C.

This demonstrates that smaller time steps can improve the accuracy of Euler's method.

## 7. New Real-World Application
Euler's method was adapted to model battery voltage discharge.

A battery starting at 5 volts was modelled using a discharge constant of 0.08 per hour. After 10 hours, the estimated voltage was approximately 2.21 volts.

This demonstrates how numerical methods can help predict battery performance.

## 8. Interpretation
The results show that Euler's method can estimate changing quantities over time. The smaller time step produced a more accurate cooling prediction, while the battery example demonstrated another practical application.

## 9. Conclusion
Euler's method is a useful numerical technique for modelling dynamic systems. It can be applied to cooling, battery discharge, population growth and other real-world processes.