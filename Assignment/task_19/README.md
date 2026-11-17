# Task 19: Numerical Optimization

## 1. Objective
To use SciPy's optimization function to find the most cost-effective allocation of resources while satisfying minimum processing capacity requirements.

## 2. Mathematical Concept
Optimization finds input values that minimize or maximize an objective function while satisfying constraints.

This task uses `scipy.optimize.minimize`.

## 3. Original Problem
A cloud service needs to allocate two types of servers at the lowest possible operating cost.

Input values:

| Variable | Type A | Type B |
|---|---:|---:|
| Cost | 12 | 18 |
| Processing capacity | 100 | 170 |

Required minimum processing capacity: 1000 units.

Objective function:

**Minimize C = 12x + 18y**

Capacity constraint:

**100x + 170y >= 1000**

Both allocations must be non-negative.

## 4. Tools Used
- Python
- NumPy
- SciPy
- Matplotlib
- VS Code

## 5. Original Results
The optimization recommended approximately:
- Type A allocation: 0
- Type B allocation: 5.882
- Total capacity: 1000 units
- Minimum operating cost: 105.88

Type B was more cost-effective because it provided more processing capacity per unit of cost.

## 6. Modified Experiment
The required processing capacity was increased from 1000 to 1200 units.

The new optimized allocation was approximately:
- Type A: 0
- Type B: 7.059
- Minimum cost: 127.06

The increased capacity requirement resulted in a higher operating cost.

## 7. New Real-World Application
The optimization model was adapted to cybersecurity log processing.

A security monitoring system required a processing capacity of 900 units. The optimized solution allocated 6 Type B resources at a total cost of 96 units.

This demonstrates how optimization can help manage computing resources used in security monitoring systems.

## 8. Interpretation
The results show that optimization helps identify cost-effective resource allocations. Increasing the required capacity increases the minimum cost, while selecting resources with better capacity-to-cost ratios reduces expenses.

The model assumes continuous resource allocations. Actual whole-server purchasing decisions would require integer comparisons.

## 9. Conclusion
Numerical optimization is useful in cloud computing, cybersecurity, engineering and resource management. SciPy's `minimize` function provides an effective way to find solutions that satisfy constraints while reducing costs.