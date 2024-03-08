bilangan = int(input("Masukkan Bilangan: "))

if bilangan %2==0 and bilangan >0:
     hasil = "Bilangan Genap Dan Positif"
elif bilangan %2==0 and bilangan <0:
     hasil = "Bilangan Genap Dan Negatif"
elif bilangan %2!=0 and bilangan <0:
     hasil = "Bilangan Ganjil Dan Negatif"
elif bilangan %2!=0 and bilangan >0:
     hasil = "Bilangan Ganjil Dan Positif"
else:
     hasil = "0 netral"

print(hasil)