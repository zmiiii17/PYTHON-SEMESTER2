num = [7, 4, 9, 2, 5, 1]

i = 0
while i < len(num):
    if num[i] % 2 != 0:
        del num[i]
    else:
        i += 1
num.sort()

print(num)