# Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
number1 = int(input("Give the first number \n"))
number2 = int(input("Give the Second number"))
result = number1 * number2
if result <= 1000:
    print(f"Product of {number1} and {number2} is: {result}")
else:
    result = number1 + number2
    print(f"Sum of {number1} and {number2} is {result}")