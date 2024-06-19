def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Get user input
n = int(input("Enter a number: "))

# Print the result
print("Factorial of {} is: {}".format(n, factorial(n)))
