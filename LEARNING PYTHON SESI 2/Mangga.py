kilo = int(input("Berapa kilogram yang akan dibeli: "))

if kilo <= 2:
    harga = 20000
elif kilo <= 5:
    harga = 18000
elif kilo <= 5:
    harga = 16000
totalHarga = kilo * harga

print ("harga yang harus dibayar jika membeli %i kilo mangga adalah %i(kilo, totalHarga)")