gajiBulanan = float(input("Gaji bulanan: "))
masukKerja = int(input("Berapa hari anda masuk kerja: "))
uangTransport = 100000 * masukKerja
uangMakan = 50000 * masukKerja
jamLembur = int(input("Berapa jam kerja lembur anda: "))

if jamLembur <= 2:
    totalLembur = jamLembur * 10000
else :
    totalLembur = 2 * 100000 + ( jamLembur -2 ) * 150000
    honor = gajiBulanan+uangTransport+uangMakan+totalLembur

    print("Uang honor yang didapat Rp.%i"honor)