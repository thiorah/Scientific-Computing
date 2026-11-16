# Task 08: Iterative Methods for Linear Systems

## 1. Objective

To solve systems of linear equations using the Jacobi and Gauss-Seidel iterative methods and compare their convergence.

## 2. Mathematical Concept

Jacobi and Gauss-Seidel methods start with an initial estimate and repeatedly improve the unknown values until the difference between successive estimates falls below a specified tolerance.

Jacobi uses values from the previous iteration, while Gauss-Seidel immediately uses newly calculated values.

## 3. Original Problem

A steady-state temperature model uses five interior grid points between two boundaries.

The left boundary is 100°C, while the right boundary is 20°C. The objective is to estimate the temperatures at the five interior points.

## 4. Input Values

- Five interior grid points.
- Left boundary temperature: 100°C.
- Right boundary temperature: 20°C.
- Initial estimates: zero.
- Tolerance: 0.00000001.
- Maximum iterations: 500.

## 5. Mathematical Operations

The system is represented as Ax = b.

The program implements:
- Jacobi iterative method.
- Gauss-Seidel iterative method.
- Maximum absolute change between successive estimates.
- Direct solution using `np.linalg.solve()` for comparison.

## 6. Original Results

Both iterative methods calculate approximately:

80°C, 60°C, 40°C, 20°C and 20°C.

The results are compared with the direct NumPy solution to verify their accuracy.

## 7. Modified Experiment

The boundary temperatures were changed to 80°C on the left and 40°C on the right.

The estimated temperatures became approximately:

64°C, 48°C, 32°C, 16°C and 28°C.

This demonstrates how changing the boundary conditions affects the temperature distribution.

## 8. Related Real-World Application

A cooling panel was modelled using a left boundary of 60°C and a right boundary of 20°C.

The Gauss-Seidel method estimated the interior temperatures as approximately:

48°C, 36°C, 24°C, 12°C and 16°C.

This demonstrates how iterative methods can help model heat distribution in cooling systems.

## 9. Graph Interpretation

The convergence graph displays the maximum change between successive iterations.

A decreasing error indicates that the estimates are approaching a stable solution. Comparing the two curves helps show the convergence behaviour of Jacobi and Gauss-Seidel.

## 10. Assumptions

- The temperature model is steady-state.
- The five interior points are connected in a one-dimensional grid.
- The coefficient matrix remains constant.
- The model uses fixed boundary temperatures.
- The iterative methods are expected to converge for this diagonally dominant matrix.

## 11. Conclusion

Jacobi and Gauss-Seidel are useful methods for solving large systems of linear equations iteratively. They can be applied to temperature modelling, electrical networks and scientific simulations. The convergence graph helps assess how quickly the methods approach an accurate solution.