# Task 11: Newton-Raphson and Secant Methods

## 1. Objective

To calculate the Internal Rate of Return (IRR) of an investment using Newton-Raphson and Secant numerical methods.

## 2. Mathematical Concept

Newton-Raphson calculates a root using:

x(n+1) = x(n) - f(x(n))/f'(x(n))

The Secant method estimates the derivative using two previous points instead of calculating it directly.

Both methods are used to find values that make a function equal to zero.

## 3. Original Problem

An investment of 10,000 is made initially, followed by annual cash inflows of 3,000, 3,500, 4,000 and 2,500.

The objective is to calculate the interest rate that makes the Net Present Value equal to zero.

## 4. Input Values

- Initial investment: -10,000
- Year 1: 3,000
- Year 2: 3,500
- Year 3: 4,000
- Year 4: 2,500
- Newton initial estimate: 0.10
- Secant initial estimates: 0.05 and 0.20

## 5. Mathematical Operations

The program uses:

- NPV calculation to determine the present value of cash flows.
- Derivative calculation for Newton-Raphson.
- `scipy.optimize.root_scalar()` with the Newton method.
- `scipy.optimize.root_scalar()` with the Secant method.
- NPV verification to confirm the calculated IRR.

## 6. Original Results

Both methods calculate approximately the same Internal Rate of Return.

The NPV at the calculated rate is approximately zero, confirming that the investment satisfies the required condition.

## 7. Modified Experiment

The Year 3 cash inflow was increased from 4,000 to 5,000.

The program recalculates the IRR using both methods.

The increased cash inflow improves the investment return and increases the calculated IRR.

## 8. Related Real-World Application

A separate business investment project was modelled using an initial investment of 15,000 and four years of projected cash inflows.

Newton-Raphson and Secant methods were used to estimate its Internal Rate of Return.

## 9. Assumptions

- Cash flows occur at the end of each year.
- The initial investment occurs at Year 0.
- The cash flow estimates are accurate.
- The interest rate is greater than -1.
- The numerical methods converge from the selected initial estimates.

## 10. Graph Interpretation

The graph shows how NPV changes as the interest rate increases. The point where the curve crosses zero represents the Internal Rate of Return.

## 11. Conclusion

Newton-Raphson and Secant methods can calculate the Internal Rate of Return of an investment. Both methods provide approximately similar results and demonstrate how numerical root-finding techniques can support financial decision-making.