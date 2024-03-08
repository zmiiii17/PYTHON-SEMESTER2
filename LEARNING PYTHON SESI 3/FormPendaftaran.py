nama = input("Masukan nama lengkap anda : ")
tempatLahir = input("Di kota mana anda lahir : ")
tanggalLahir = int(input("Masukan tanggal lahir anda : "))
tahunLahir = int(input("Tahun berapa anda lahir : "))
jenisKelamin = input("Masukan jenis kelamin anda : ")
english = float(input("Masukan nilai bahasa Inggris anda : "))
mtk = float(input("Masukan nilai Matematika anda : "))
indonesia = float(input("Masukan nilai bahasa Indonesia anda : "))

nilaiRerata = (english + mtk + indonesia) / 3
tahunSekarang = 2024
umur = tahunSekarang - tahunLahir

if umur > 25:
    print(nama, "yang berumur", umur, "tahun, tidak memenuhi syarat untuk mendaftar ke Institut Teknologi Bandung")
elif nilaiRerata >= 80 and jenisKelamin == "Pria":
    print(nama, "disarankan masuk ke jurusan Teknik Informatika")
elif nilaiRerata >= 80 and jenisKelamin == "Wanita":
    print(nama, "disarankan masuk Sistem Informasi")
else:
    print(nama, "disarankan masuk DKV")
    