# Import the logo from the art module
from art import logo

# Define function to add two numbers
def add(n1, n2):
  return n1 + n2

# Define function to subtract two numbers
def subtract(n1, n2):
  return n1 - n2

# Define function to multiply two numbers
def multiply(n1, n2):
  return n1 * n2

# Define function to divide two numbers
def divide(n1, n2):
  return n1 / n2

# Create a dictionary to store arithmetic operations
operation = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide 
}

# Define the calculator function
def calculator():
  # Print the calculator logo
  print(logo)

  # Prompt the user to enter the first number
  num_1 = float(input("Pick a number: "))

  # Display the arithmetic operation options
  for symbols in operation:
    print(symbols)

  # Initialize a variable to control the loop
  should_continue = True

  # Start the loop for continuous calculation
  while should_continue:
    # Prompt the user to select an operation
    operation_symbol = input("Pick an operation: ")

    # Prompt the user to enter the second number
    num_2 = float(input("Pick another number: "))

    # Select the appropriate arithmetic function based on user input
    calculate_operation = operation[operation_symbol]

    # Perform the selected operation and store the result
    answer = calculate_operation(num_1, num_2)

    # Print the result of the calculation
    print(f"{num_1} {operation_symbol} {num_2} = {answer}")

    # Prompt the user if they want to continue or exit
    if input(f"Type 'y' to continue with {answer} or 'n' to exit:\n") == "y":
      num_1 = answer
    else:
      should_continue = False
      calculator()  # Restart the calculator if user wants to continue

# Call the calculator function to start the program
calculator()

  