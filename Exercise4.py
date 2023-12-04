def same_or_not(numbers):
    return numbers[0] == numbers[-1]
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 25, 30]
x = same_or_not(numbers_x)
y = same_or_not(numbers_y)
print("For numbers_x:", x)
print("For numbers_y:", y)