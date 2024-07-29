def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]
    
    return median

# 使用例
numbers = [10, 3, 5, 7, 2]
result = calculate_average(numbers)
print(result) 
