def find_max_value(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

numbers = [10, 3, 5, 7, 2]
result = find_max_value(numbers)
print(result)
