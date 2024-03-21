a = 1
b = 2
c = 3

print(a, end=" ")
print(b, end=" ")
print(c, end=" ")

r = 7 
for i in range (r):
    next_num = a + b + c 
    print(next_num, end=" ")
    
    a = b
    b = c
    c = next_num
