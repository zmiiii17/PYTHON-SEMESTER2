def skorToBobot (nilai) :
    if nilai >= 90:
        return 4.00 
    elif nilai >= 85:
        return 3.75
    elif nilai >= 80:
        return 3.50
    elif nilai >= 75:
        return 3.25
    elif nilai >= 70:
        return 3.00 
    elif nilai >= 65:
        return 2.75
    elif nilai >= 60:
        return 2.50
    elif nilai >= 55:
        return 2.25
    elif nilai >= 50:
        return 2.00
    elif nilai >=45:
        return 1.75
    elif nilai >=40:
        return 1.50
    elif nilai >= 35:
        return 1.25
    elif nilai >= 30:
        return 1.00
    else :
        return 0.00
    
algoritma = float(input("Masukan nilai akhir mata kuliah Algoritma anda : "))
sksAlgoritma = 4
totalAlgoritma = sksAlgoritma * skorToBobot(algoritma)
pbo = float(input("Masukan nilai akhir mata kuliah PBO anda : "))
sksPbo = 3
totalPbo = sksPbo * skorToBobot(pbo)
kalkulus = float(input("Masukan nilai akhir mata kuliah Kalkulus anda : "))
sksKalkulus = 3
totalKalkulus = sksKalkulus * skorToBobot(kalkulus)
etikaProfesi = float(input("Masukan nilai akhir mata kuliah Etika Profesi anda : "))    
sksEtika = 2
totalEtika = sksEtika * skorToBobot(etikaProfesi)
databases = float(input("Masukan nilai akhir mata kuliah Database anda : "))
sksDatabases = 4
totalDatabase = sksDatabases * skorToBobot(databases)
english = float(input("Masukan nilai akhir mata kuliah English anda : ")) 
sksEnglish = 2
totalEnglish = sksEnglish * skorToBobot(english)

totalSks = sksAlgoritma + sksPbo + sksKalkulus + sksEtika + sksDatabases + sksEnglish

IPK = (totalAlgoritma + totalPbo + totalKalkulus + totalEtika + totalDatabase + totalEnglish) / totalSks

print("Nilai IPK anda adalah", IPK)