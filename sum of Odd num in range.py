def sum_of_odd_numbers(range_limit):
    sum_odd = 0
    for num in range(1, range_limit + 1, 2):
        sum_odd += num
    return sum_odd

range_limit = int(input("Enter the range limit: "))
result = sum_of_odd_numbers(range_limit)
print("The sum of odd numbers up to", range_limit, "is:", result)
