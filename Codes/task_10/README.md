# Task 10: Root Finding — Bisection and Fixed-Point Methods

## 1. Objective

To find the root of a nonlinear heat-balance equation using the Bisection and Fixed-Point methods.

## 2. Mathematical Concept

A root is a value that makes a function equal to zero.

The Bisection method repeatedly divides an interval containing a root into two smaller intervals.

The Fixed-Point method rearranges an equation into the form T = g(T) and repeatedly calculates new estimates until they stabilize.

## 3. Original Problem

The task models a heat-balance system to determine its equilibrium temperature.

The equation used is:

f(T) = T - 25 - 10e^(-T/20)

The objective is to find the temperature where f(T) = 0.

## 4. Input Values

- Initial Bisection interval: 20 to 40.
- Initial Fixed-Point estimate: 30°C.
- Base temperature parameter: 25.
- Heat contribution parameter: 10.
- Fixed-Point maximum iterations: 100.
- Tolerance: 0.0000000001.

## 5. Mathematical Operations

The program uses:

- `scipy.optimize.root_scalar()` with the Bisection method.
- Exponential calculations using NumPy.
- Repeated substitution for Fixed-Point iteration.
- Function evaluation to verify the calculated roots.
- Matplotlib to plot the heat-balance function.

## 6. Original Results

Both methods calculate an equilibrium temperature of approximately 27.525211°C.

The Fixed-Point method converges in approximately 13 iterations.

The verification values are approximately zero, confirming that the calculated temperature satisfies the equation.

## 7. Modified Experiment

The base temperature parameter was increased from 25 to 30.

The new equilibrium temperature became approximately 32.206042°C.

This shows how changing a model parameter affects the calculated equilibrium.

## 8. Related Real-World Application

A simplified refrigeration chamber heat-balance model was introduced using a base temperature parameter of 30 and a heat contribution parameter of 8.

The Bisection method was used to determine its equilibrium temperature.

## 9. Graph Interpretation

The graph shows the heat-balance function against temperature. The point where the curve crosses the horizontal zero line represents the equilibrium temperature.

## 10. Assumptions

- The heat-balance equation represents the system.
- The model parameters remain constant during each calculation.
- The Bisection interval contains a root.
- Fixed-Point iteration converges for the chosen rearranged equation.
- The model is illustrative rather than a complete physical refrigeration model.

## 11. Conclusion

The Bisection and Fixed-Point methods successfully determine the root of the heat-balance equation. Both methods produce approximately the same equilibrium temperature, demonstrating their usefulness in solving nonlinear scientific and engineering problems.