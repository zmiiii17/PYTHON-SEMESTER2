numbers = [8, 3, 12, 0, 7, 2]

for i in range(len(numbers)):
    if numbers[i] < 5:
        numbers[i] = 0

numbers.sort(reverse=True)

print(numbers)