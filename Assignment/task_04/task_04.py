
from decimal import Decimal
import math


print("TASK 04: FLOATING-POINT ARITHMETIC AND NUMERICAL ERRORS")

# PART 1: A common floating-point example
a = 0.1
b = 0.2
c = 0.3

result = a + b

print("\n--- Part 1: Floating-Point Representation ---")
print("0.1 + 0.2 =", result)
print("Expected value:", c)
print("Exactly equal to 0.3?", result == c)
print("Close to 0.3?", math.isclose(result, c))


# PART 2: Compare floating-point and exact decimal arithmetic
decimal_result = Decimal("0.1") + Decimal("0.2")

print("\n--- Part 2: Decimal Arithmetic ---")
print("Float result:", result)
print("Decimal result:", decimal_result)
print("Decimal equals 0.3?",
      decimal_result == Decimal("0.3"))


# PART 3: Repeated addition and accumulated error
number_of_additions = 100_000

float_total = 0.0

for _ in range(number_of_additions):
    float_total += 0.1

expected_total = number_of_additions * 0.1
error = float_total - expected_total

print("\n--- Part 3: Accumulated Error ---")
print("Number of additions:", number_of_additions)
print("Expected total:", expected_total)
print("Floating-point total:", float_total)
print("Accumulated error:", error)


# PART 4: Change a parameter
modified_additions = 1_000_000

modified_total = 0.0

for _ in range(modified_additions):
    modified_total += 0.1

modified_expected = modified_additions * 0.1
modified_error = modified_total - modified_expected

print("\n--- Part 4: Modified Experiment ---")
print("Number of additions:", modified_additions)
print("Expected total:", modified_expected)
print("Floating-point total:", modified_total)
print("Accumulated error:", modified_error)


# PART 5: Real-world application - financial calculations
# Demonstrate why Decimal is useful for decimal currency amounts.
price = Decimal("19.99")
quantity = 3
discount = Decimal("5.00")

total_cost = price * quantity - discount

print("\n--- Part 5: Financial Calculation ---")
print("Price per item: $", price, sep="")
print("Quantity:", quantity)
print("Discount: $", discount, sep="")
print("Final cost: $", total_cost.quantize(Decimal("0.01")), sep="")
