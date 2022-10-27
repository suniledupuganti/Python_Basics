# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
number = int(input("Enter the range value: "))
print(f"Printing Current and Previous number sum in range of {number}")
previous_number = 0
for i in range(number):
    current_number = i
    result = current_number + previous_number
    print(f"Current Number {current_number} Previous Number {previous_number} Sum: {result}")
    previous_number = current_number
