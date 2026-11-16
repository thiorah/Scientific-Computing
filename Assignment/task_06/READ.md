# Task 06: Solution of Systems of Linear Equations

## 1. Objective

To solve simultaneous linear equations using Python and NumPy.

## 2. Original Problem

A data centre has two server types with different CPU and memory requirements. The objective is to determine the number of active servers using their total resource consumption.

## 3. Input Values

- Type A: 4 CPU units and 8 GB memory.
- Type B: 2 CPU units and 12 GB memory.
- Total CPU usage: 20 units.
- Total memory usage: 72 GB.

## 4. Mathematical Operations

The equations are:

4x + 2y = 20

8x + 12y = 72

They are represented using the matrix equation Ax = b.

The program uses `np.linalg.solve(A, b)` to calculate the unknown values.

## 5. Original Results

The program calculates:

- Type A: 3 servers.
- Type B: 4 servers.

The calculated resource usage matches the expected values, and the residual is zero.

## 6. Modified Input

The total CPU usage was changed to 24 units, while memory usage was changed to 96 GB.

The new results were:

- Type A: 3 servers.
- Type B: 6 servers.

This demonstrates how changing input values affects the solution.

## 7. Related Real-World Application

A different data-centre configuration was introduced.

- Type A: 6 CPU units and 8 GB memory.
- Type B: 2 CPU units and 16 GB memory.
- Total CPU usage: 18 units.
- Total memory usage: 64 GB.

The program calculated two Type A servers and three Type B servers.

## 8. Assumptions

- Each server type has fixed CPU and memory requirements.
- Total resource consumption is known.
- The equations represent the combined resource usage.
- Server quantities are expected to be non-negative whole numbers.

## 9. Conclusion

Systems of linear equations can be used to calculate unknown quantities from known values. NumPy's `linalg.solve()` function provides an efficient way to solve these equations and verify the results. This method can support resource allocation and data-centre planning.