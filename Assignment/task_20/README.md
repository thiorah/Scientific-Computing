# Task 20: Random Numbers and Monte Carlo Methods

## 1. Objective
To use random sampling and Monte Carlo simulation to estimate probabilities and understand how repeated simulations can model uncertain real-world situations.

## 2. Mathematical Concept
Monte Carlo methods use repeated random sampling to estimate quantities or probabilities.

The probability of an event is estimated using:

**Probability = Number of successful events / Total simulations**

## 3. Original Problem
The program estimates the probability that a network server becomes overloaded.

Input values:
- Server capacity: 1000 units
- Mean demand: 850 units
- Standard deviation: 120 units
- Number of simulations: 100,000
- Random seed: 42

Incoming demand is generated using a normal distribution.

## 4. Tools Used
- Python
- NumPy
- Matplotlib
- VS Code

## 5. Original Results
Out of 100,000 simulated demand scenarios, 10,616 exceeded the server capacity.

The estimated overload probability was 10.616%.

## 6. Modified Experiment
Server capacity was increased from 1000 to 1100 units.

The estimated overload probability decreased from 10.616% to 1.912%.

This demonstrates that increasing server capacity reduces the likelihood of overload under the assumed demand distribution.

## 7. New Real-World Application
Monte Carlo simulation was adapted to model cybersecurity attack attempts.

The simulation assumed 100 suspicious attempts per monitoring period, with each attempt having a 2% probability of success.

A monitoring period with at least 5 successful attempts was classified as high-risk.

Out of 100,000 simulated periods, 5,080 were high-risk, giving an estimated probability of 5.08%.

These are illustrative assumptions rather than measured real-world attack statistics.

## 8. Interpretation
The results show that Monte Carlo methods can estimate risks by generating many possible scenarios. Increasing the number of simulations generally makes probability estimates more stable.

## 9. Conclusion
Monte Carlo simulation is useful in risk analysis, network reliability, cybersecurity, finance and scientific modelling. It helps estimate the likelihood of uncertain events and supports better decision-making.