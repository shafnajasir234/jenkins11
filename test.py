import sys

# Check if two arguments are provided
if len(sys.argv) != 3:
    print("Usage: python3 test.py <number1> <number2>")
    sys.exit(1)

# Convert command-line arguments to floats
number1 = float(sys.argv[1])
number2 = float(sys.argv[2])

# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Calculate the sum
result = add_numbers(number1, number2)

# Display the result
print(f"The sum of {number1} and {number2} is: {result}")
echo
