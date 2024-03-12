bilangan = int(input("Masukkan Angka A: "))

if bilangan >0:
    hasil = "bilangan %i adalah positif"%(bilangan)
elif bilangan <0:
    hasil = "bilangan %i adalah negatif"%(bilangan)
else :
    hasil = "bilangan %i adalah netral"%(bilangan)

print(hasil)