def sum_of_even_numbers(range_limit):
    sum_even = 0
    for num in range(2, range_limit + 1, 2):
        sum_even += num
    return sum_even

range_limit = int(input("Enter the range limit: "))
result = sum_of_even_numbers(range_limit)
print("The sum of even numbers up to", range_limit, "is:", result)
