# Task 04: Floating-Point Arithmetic and Numerical Errors

## 1. Objective

To investigate floating-point representation, rounding errors and accumulated numerical errors using Python.

## 2. Original Problem

The program investigates why adding 0.1 and 0.2 using floating-point arithmetic may not produce exactly 0.3.

## 3. Mathematical Operations

The program performs decimal addition, repeated addition and error calculation.

Error = Calculated total - Expected total.

It also compares Python floating-point arithmetic with the Decimal class.

## 4. Original Results

The calculation 0.1 + 0.2 typically produces 0.30000000000000004. The result is not exactly equal to the floating-point value 0.3, but it is numerically close.

Using Decimal with string inputs produces the exact decimal result 0.3.

## 5. Modified Experiment

The number of repeated additions was increased from 100,000 to 1,000,000.

Record the expected total, calculated total and accumulated error from the program output. Compare the two experiments to explain how the number of operations affects numerical error.

## 6. Related Real-World Application

The program calculates the cost of three items priced at $19.99 each, with a $5.00 discount. Decimal arithmetic gives a final cost of $54.97.

This demonstrates the usefulness of decimal arithmetic for financial calculations that require predictable decimal representation.

## 7. Assumptions

- The floating-point values use Python's standard float representation.
- The expected totals are used as comparison values for the experiments.
- The financial example uses decimal currency values and a discount applied before final rounding.

## 8. Conclusion

Floating-point arithmetic can introduce small representation and rounding errors. Repeated operations allow these errors to accumulate. Decimal arithmetic is useful when exact decimal representation is required, particularly in financial calculations.