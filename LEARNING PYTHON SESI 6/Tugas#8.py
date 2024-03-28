row = 5
karakter = ["S","O"]

for i in range (row):
    for j in range (row - i):
        print(karakter[(i + j) % 2], end=" ")
    print( )