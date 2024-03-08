nilai = int(input("Masukkan Nilai: "))

if nilai < 50 :
    keterangan = "Nilai E"
elif nilai < 60 :
    keterangan = "Nilai D"
elif nilai < 70 :
    keterangan = "Nilai C"
elif nilai < 80 :
    keterangan = "Nilai B"
else :
    keterangan = "Nilai A"

    
print(keterangan)