def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    total_sum = 0
    for i in range(len(numbers)):
        for j in range(i + 1):
            total_sum += numbers[j]
        total_sum -= sum(numbers[:i])

    average = total_sum / len(numbers)
    return average

# 使用例
numbers = [10, 3, 5, 7, 2]
result = calculate_average(numbers)
print(result)  # 出力は 5.4（平均値）
