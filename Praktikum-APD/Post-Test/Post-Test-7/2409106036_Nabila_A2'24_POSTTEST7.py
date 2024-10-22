pengguna = {
    "nabila": {
        "password": "036",
        "transaksi": {}
    }
}

def menu_utama():
    print("""
    =================================
    |        Jurnal Keuangan        |
    =================================
    |      1. Register              |
    |      2. Login                 |
    |      3. Exit                  |
    =================================
    """)

def register():
    username = input("Buat username: ")
    password = input("Buat password: ")
    
    if username in pengguna:
        print("Username sudah digunakan.")
        ulangi = input("apakah anda ingin login ulang? [Y/N] ")
        if ulangi == 'Y':
            login()
        else:
            print("kembali ke menu utama")
    else:
        pengguna[username] = {"password": password, "transaksi": {}}
        print("Pendaftaran berhasil!")

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in pengguna and pengguna[username]["password"] == password:
        if username == "nabila":
            print("Login berhasil! Selamat datang Admin.")
            menu_admin(username)
        else:
            print(f"Login berhasil! Selamat datang, {username}.")
            menu_user(username)
    else:
        print("Username atau password salah.")
        ulangi = input("apakah anda ingin login ulang? [Y/N] ")
        if ulangi == 'Y':
            login()
        else:
            print("kembali ke menu utama")

def menu_admin(username):
    print("""
    Login berhasil! Selamat datang admin
    ===============================================
    |                    MENU                     |
    ===============================================
    |    1. Tambah Transaksi                      |           
    |    2. Tampilkan Semua Transaksi Pengguna    |    
    |    3. Ubah Transaksi                        |     
    |    4. Hapus Transaksi                       |
    |    5. Keluar                                |        
    ===============================================
    """)

    while True:
        pilihan_admin = int(input("Pilih opsi: "))
        if pilihan_admin == 1:
            tambah_transaksi(username)
        elif pilihan_admin == 2:
            tampilkan_semua_transaksi()
        elif pilihan_admin == 3:
            ubah_transaksi(username)
        elif pilihan_admin == 4:
            hapus_transaksi(username)
        elif pilihan_admin == 5:
            print("Terima kasih telah mengakses jurnal keuangan")
            break
        else:
            print("Anda salah input")

def menu_user(username):
    print(f"Login berhasil! Selamat datang, {username}.")
    print("""
    =================================
    |             MENU              |
    =================================
    |    1. Tambah Transaksi        |           
    |    2. Tampilkan Transaksi     |    
    |    3. Ubah Transaksi          |     
    |    4. Hapus Transaksi         |
    |    5. Keluar                  |        
    =================================
    """)

    while True:
        pilihan_user = int(input("Pilih opsi: "))
        if pilihan_user == 1:
            tambah_transaksi(username)
        elif pilihan_user == 2:
            tampilkan_transaksi(username)
        elif pilihan_user == 3:
            ubah_transaksi(username)
        elif pilihan_user == 4:
            hapus_transaksi(username)
        elif pilihan_user == 5:
            print("Terima kasih telah menggunakan Jurnal Keuangan")
            break
        else:
            print("Anda salah input")

def tambah_transaksi(username):
    tanggal = input("Masukkan tanggal (DD/MM/YYYY): ")
    deskripsi = input("Masukkan deskripsi transaksi: ")
    jumlah = int(input("Masukkan jumlah ('+' untuk pemasukan, '-' untuk pengeluaran): "))
    pengguna[username]["transaksi"][tanggal] = {"deskripsi": deskripsi, "jumlah": jumlah}
    print("Transaksi berhasil ditambahkan!")

def tampilkan_semua_transaksi():
    for username, data in pengguna.items():
        print(f"\nData Pengguna: {username}")
        if data["transaksi"]:
            for tanggal, transaksi in data["transaksi"].items():
                print(f"Tanggal: {tanggal}, Deskripsi: {transaksi['deskripsi']}, Jumlah: {transaksi['jumlah']}")
        else:
            print("Tidak ada transaksi.")

def tampilkan_transaksi(username):
    print(f"Transaksi {username}:")
    if pengguna[username]["transaksi"]:
        for tanggal, transaksi in pengguna[username]["transaksi"].items():
            print(f"Tanggal: {tanggal}, Deskripsi: {transaksi['deskripsi']}, Jumlah: {transaksi['jumlah']}")
    else:
        print("Tidak ada transaksi.")

def ubah_transaksi(username):
    tanggal_lama = input("Masukkan tanggal transaksi yang ingin diubah: ")
    if tanggal_lama in pengguna[username]["transaksi"]:
        tanggal_baru = input("Masukkan tanggal baru (DD/MM/YYYY): ")
        deskripsi_baru = input("Masukkan deskripsi baru: ")
        jumlah_baru = int(input("Masukkan jumlah baru: "))
        pengguna[username]["transaksi"].pop(tanggal_lama)
        pengguna[username]["transaksi"][tanggal_baru] = {"deskripsi": deskripsi_baru, "jumlah": jumlah_baru}
        print("Transaksi berhasil diubah!")
    else:
        print("Transaksi tidak ditemukan.")

def hapus_transaksi(username):
    tanggal_hapus = input("Masukkan tanggal transaksi yang ingin dihapus: ")
    if tanggal_hapus in pengguna[username]["transaksi"]:
        pengguna[username]["transaksi"].pop(tanggal_hapus)
        print(f"Transaksi pada tanggal {tanggal_hapus} berhasil dihapus.")
    else:
        print("Transaksi tidak ditemukan.")

def main():
    while True:
        menu_utama()
        pilihan = int(input("Pilih opsi: "))
        if pilihan == 1:
            register()
        elif pilihan == 2:
            login()
        elif pilihan == 3:
            print("Terima kasih telah menggunakan Jurnal Keuangan ini.")
            break
        else:
            print("Opsi tidak valid.")

main()