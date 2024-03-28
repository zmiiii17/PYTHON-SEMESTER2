sequence = [0,1]
limit   = 10

while len (sequence) < limit:
    next_num = sequence[-1] + sequence [-2]
    sequence.append(next_num)
    
for num in sequence:
    for _ in range(num):
        print("*", end=" ")
    print()