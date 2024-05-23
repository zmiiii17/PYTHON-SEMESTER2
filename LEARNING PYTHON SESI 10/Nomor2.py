angka= [7, 4, 9, 2, 5, 1]

i=0
while i < len(angka):
    if angka[i] %2 != 0:
        del angka[i]
    else:
        i += 1
           
angka.sort()

    
print(angka)