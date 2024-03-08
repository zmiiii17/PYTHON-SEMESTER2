umur = int(input("Masukan umur : "))

if umur <= 2 :
    print("Bayi")
elif umur <= 5 :
    print("Balita")
elif umur <= 12 :
    print("Anak-anak")
elif umur <= 17 :
    print("Remaja")
elif umur < 30 :
    print("Dewasa")
else :
    print("Orang tua")