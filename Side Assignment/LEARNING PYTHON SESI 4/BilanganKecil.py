Bilangan_A = int(input("Masukkan Bilangan A: "))
Bilangan_B = int(input("Masukkan Bilangan B: "))
Bilangan_C = int(input("Masukkan Bilangan C: "))

if Bilangan_A < Bilangan_B and Bilangan_C:
    hasil = "Bilangan A paling kecil dari Bilangan B dan Bilangan C"
elif Bilangan_B < Bilangan_A and Bilangan_C:
    hasil = "Bilangan B paling kecil dari Bilangan A dan Bilangan C"
else:
    hasil = "Bilangan C paling kecil dari Bilangan A dan Bilangan B"


print(hasil)