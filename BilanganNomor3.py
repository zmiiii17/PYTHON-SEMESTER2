bilangan_A = int(input("Masukkan Bilangan A: "))
bilangan_B = int(input("Masukkan Bilangan B: "))
bilangan_C = int(input("Masukkan Bilangan C: "))

if bilangan_A > bilangan_B and bilangan_A > bilangan_C:
    hasil = "bilangan %i paling besar dari %i dan %i"%(bilangan_A,bilangan_B,bilangan_C)
elif bilangan_B > bilangan_A and bilangan_B > bilangan_C:
    hasil = "bilangan %i paling besar dari %i dan %i"%(bilangan_B,bilangan_A,bilangan_C)
elif bilangan_C > bilangan_A and bilangan_C > bilangan_B:
    hasil = "bilangan %i paling besar dari %i dan %i"%(bilangan_C,bilangan_A,bilangan_C)
elif bilangan_A == bilangan_B and bilangan_A > bilangan_C:
    hasil = "bilangan %i dan %i lebih besar dari %i"%(bilangan_A,bilangan_B,bilangan_C)
elif bilangan_B == bilangan_C and bilangan_B > bilangan_A:
    hasil = "bilangan %i dan %i lebih besar dari %i"%(bilangan_B,bilangan_C,bilangan_A)
elif bilangan_C == bilangan_A and bilangan_C > bilangan_B:
    hasil = "bilangan %i dan %i lebih besar dari %i"%(bilangan_C,bilangan_A,bilangan_B)
else:
    hasil = "bilangan sama"

print(hasil)