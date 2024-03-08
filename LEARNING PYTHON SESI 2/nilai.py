English = int (input("Masukkan nilai: "))
MTK = int (input("Masukkan nilai: "))
Indo = int (input("Masukkan nilai: "))
IPA = int (input("Masukkan nilai: "))
IPS = int (input("Masukkan nilai: "))

ratarataSatu = (English + MTK + Indo) / 3
ratarataDua = (English + MTK + Indo + IPA + IPS) / 5

if ratarataSatu >=75:
    kelulusan = "lulus"
elif ratarataDua >=70:
    kelulusan = "lulus"
elif English > 90 and MTK > 90:
    kelulusan - "lulus"
else: 
    kelulusan ="tidak lulus"

print(kelulusan)




