def calculate_ceiling_average(arr):
    sum = 0
    for num in arr:
        sum += num

    average = sum / len(arr)
    ceiling_average = int(average) + (average % 1 > 0)

    return ceiling_average

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = calculate_ceiling_average(numbers)
print("Ceiling Average:", result)  # Output: Ceiling Average: 3