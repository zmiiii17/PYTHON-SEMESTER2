print ("Apa yang ingin anda coba konversi ? celcius / fahrenheit")
derajat = int(input("Angka suhu: "))
suhu = str(input("Dari jenis suhuh : "))
suhu2 = str(input("Ke jenis suhuh : "))

if suhu == "celcius":
    hasil= derajat *1.8+32
else:
    hasil = ((derajat-32)*5)/9


print(derajat, suhu, " di konversikan menjadi ",hasil, suhu2)