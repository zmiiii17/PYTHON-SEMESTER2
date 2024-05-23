buku_list = []
peminjam_list = []
list_mahasiswa = []

# Menambahkan isi buku
def tambahBuku(no_isbn, judul, pengarang, isiHalaman, deskripsi, stok, booked):
    buku = {
        "no_isbn": no_isbn,
        "judul": judul,
        "pengarang": pengarang,
        "isiHalaman": isiHalaman,
        "deskripsi": deskripsi,
        "stok": stok,
        "booked": booked
    }
    buku_list.append(buku)
    print("Buku telah ditambahkan ke dalam daftar")

# Untuk melihat buku yang tersedia
def daftarBuku():
    if not buku_list:
        print("Tidak ada buku yang tersedia")
    else:
        for buku in buku_list:
            print(f"Judul: {buku['judul']}, No ISBN: {buku['no_isbn']}, Pengarang: {buku['pengarang']}, Isi Halaman: {buku['isiHalaman']}, Deskripsi: {buku['deskripsi']}, Stok: {buku['stok']}, Booked: {buku['booked']}")

# Menambahkan mahasiswa ke daftar
def tambahMahasiswa(nama, nim, nomerhp, alamat):
    mahasiswa = {
        "nama": nama,
        "nim": nim,
        "nomerhp": nomerhp,
        "alamat": alamat
    }
    list_mahasiswa.append(mahasiswa)
    print("Mahasiswa telah ditambahkan ke dalam daftar")

# Menampilkan daftar mahasiswa
def daftarMahasiswa():
    if not list_mahasiswa:
        print("Tidak ada mahasiswa yang terdaftar")
    else:
        for mahasiswa in list_mahasiswa:
            print(f"Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}, No HP: {mahasiswa['nomerhp']}, Alamat: {mahasiswa['alamat']}")

# Menambahkan peminjam
def tambahPeminjam(nim, no_isbn, tanggalpinjam, tanggal_kembali, status):
    peminjam = {
        "nim": nim,
        "no_isbn": no_isbn,
        "tanggalpinjam": tanggalpinjam,
        "tanggalkembali": tanggal_kembali,
        "status": status
    }
    peminjam_list.append(peminjam)
    print("Peminjaman telah ditambahkan ke dalam daftar")

# Peminjaman buku
def pinjamBuku(nim, no_isbn):
    mahasiswa = next((m for m in list_mahasiswa if m['nim'] == nim), None)
    buku = next((b for b in buku_list if b['no_isbn'] == no_isbn), None)
    
    if mahasiswa and buku:
        if buku['stok'] - buku['booked'] > 0:
            buku['booked'] += 1
            tanggalpinjam = datetime.now().strftime('%Y-%m-%d')
            tanggal_kembali = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
            tambahPeminjam(nim, no_isbn, tanggalpinjam, tanggal_kembali, 'Dipinjam')
            print(f"Buku '{buku['judul']}' berhasil dipinjam oleh {mahasiswa['nama']}")
        else:
            print('Stok buku tidak mencukupi')
    else:
        print('Mahasiswa atau buku tidak ditemukan')

# Pengembalian buku
def kembalikanBuku(nim, no_isbn):
    peminjaman = next((p for p in peminjam_list if p['nim'] == nim and p['no_isbn'] == no_isbn and p['status'] == 'Dipinjam'), None)
    buku = next((b for b in buku_list if b['no_isbn'] == no_isbn), None)
    
    if peminjaman and buku:
        buku['booked'] -= 1
        peminjaman['status'] = 'Dikembalikan'
        peminjaman['tanggalkembali'] = datetime.now().strftime('%Y-%m-%d')
        print(f"Buku '{buku['judul']}' berhasil dikembalikan")
    else:
        print('Peminjaman tidak ditemukan')

def menu():
    while True:
        print("\n========== Manajemen Perpustakaan ==========")
        print("1. Tambah Buku")
        print("2. Lihat Daftar Buku")
        print("3. Tambah Mahasiswa")
        print("4. Lihat Daftar Mahasiswa")
        print("5. Pinjam Buku")
        print("6. Kembalikan Buku")
        print("7. Keluar")
        
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            no_isbn = input("Masukkan ISBN buku: ")
            judul = input("Masukkan judul buku: ")
            pengarang = input("Masukkan pengarang buku: ")
            isiHalaman = int(input("Masukkan jumlah halaman buku: "))
            deskripsi = input("Masukkan deskripsi buku: ")
            stok = int(input("Masukkan stok buku: "))
            booked = 0  # Awalnya booked adalah 0
            tambahBuku(no_isbn, judul, pengarang, isiHalaman, deskripsi, stok, booked)
        elif pilihan == '2':
            daftarBuku()
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM mahasiswa: ")
            nomerhp = input("Masukkan nomor HP mahasiswa: ")
            alamat = input("Masukkan alamat mahasiswa: ")
            tambahMahasiswa(nama, nim, nomerhp, alamat)
        elif pilihan == '4':
            daftarMahasiswa()
        elif pilihan == '5':
            nim = input("Masukkan NIM mahasiswa: ")
            no_isbn = input("Masukkan ISBN buku: ")
            pinjamBuku(nim, no_isbn)
        elif pilihan == '6':
            nim = input("Masukkan NIM mahasiswa: ")
            no_isbn = input("Masukkan ISBN buku: ")
            kembalikanBuku(nim, no_isbn)
        elif pilihan == '7':
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
menu()