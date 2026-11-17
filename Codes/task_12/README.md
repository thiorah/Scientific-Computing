# Task 12: Polynomial and Nonlinear Equation Solving

## 1. Objective

To solve a system of nonlinear equations using Python and SciPy and identify the intersection points between a circle and a parabola.

## 2. Mathematical Concept

Polynomial equations contain variables raised to different powers. Nonlinear systems contain equations that are not all linear in their unknown variables.

Numerical solvers estimate values that make the equations or residuals approach zero.

## 3. Original Problem

Find the intersection points between:

Circle: x² + y² = 4

Parabola: y = x² - 1

The two equations are solved simultaneously to determine the unknown coordinates x and y.

## 4. Input Values

- Circle radius: 2 units.
- Parabola equation: y = x² - 1.
- First initial guess: [1, 1].
- Second initial guess: [-1, 1].

## 5. Mathematical Operations

The program defines two residual equations:

f1(x,y) = x² + y² - 4

f2(x,y) = y - (x² - 1)

It uses `scipy.optimize.root()` to solve the equations from different initial guesses.

The residual values are checked to verify the accuracy of the calculated intersections.

## 6. Original Results

The two intersection points are approximately:

- (1.5175, 1.3028)
- (-1.5175, 1.3028)

The residuals are approximately zero, indicating that the calculated points satisfy both equations.

## 7. Modified Experiment

The circle radius was increased from 2 to 3 units.

The new intersection points became approximately:

- (1.8364, 2.3723)
- (-1.8364, 2.3723)

This demonstrates how changing the circle's radius affects its intersection with the parabola.

## 8. Related Real-World Application

A simplified wireless coverage model was considered, where a circular coverage boundary intersects a parabolic signal path.

The nonlinear solver identifies the intersection coordinates, which can represent locations where the modelled path meets the coverage boundary.

## 9. Assumptions

- The circle and parabola are represented by mathematical equations.
- The wireless coverage area is circular.
- The parabolic path is a simplified model.
- The coordinates are measured in arbitrary units.
- The solver uses suitable initial estimates to locate the intersections.

## 10. Graph Interpretation

The graph displays the original and modified circles together with the parabola. Their intersection points represent the solutions of the nonlinear system.

## 11. Conclusion

Nonlinear equation solving is useful for finding unknown values in systems involving multiple mathematical relationships. SciPy's root function can solve such systems numerically, while residual calculations help verify the accuracy of the results.