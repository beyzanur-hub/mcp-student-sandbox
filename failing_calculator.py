def average_ratios(numbers):
    total = 0
    count = 0
    for num in numbers:
        if num != 0:
            total += 100 / num
            count += 1
    return total / count if count > 0 else 0

print(average_ratios([10, 5, 0]))
