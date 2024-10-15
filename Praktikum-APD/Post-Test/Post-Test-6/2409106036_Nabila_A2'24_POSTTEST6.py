print(
    """
Selamat datang di Jurnal Keuangan!
===========================
|   SILAHKAN PILIH OPSI   |
===========================
|    1. REGISTER          |           
|    2. LOGIN             |          
|    3. EXIT              |       
===========================
"""
)

pengguna = {
    "nabila": {
        "password": "036",
        "transaksi": {}
    }
}

while True:
    pilihan = int(input("Pilih opsi: "))

    if pilihan == 1:
        username = input("Buat username: ")
        password = input("Buat password: ")

        if pengguna.get(username):
            print("Error: Username sudah digunakan")
        else:
            pengguna[username] = {"password": password, "transaksi": {}}
            print("Pendaftaran berhasil!")

    elif pilihan == 2:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if pengguna.get(username) and pengguna[username]["password"] == password:
            if username == "nabila":
                print(
                    """
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
                    """
                )

                while True:
                    pilihan_admin = int(input("Pilih opsi: "))

                    if pilihan_admin == 1:
                        tanggal = input("Masukkan tanggal (DD/MM/YYYY): ")
                        deskripsi = input("Masukkan deskripsi transaksi: ")
                        jumlah = int(input("Masukkan jumlah ('+' untuk pemasukan, '-' untuk pengeluaran): "))
                        pengguna[username]["transaksi"][tanggal] = {"deskripsi": deskripsi, "jumlah": jumlah}
                        print("Transaksi berhasil ditambahkan!")

                    elif pilihan_admin == 2:
                        print("Semua Transaksi Pengguna:")
                        for user, data in pengguna.items():
                            print(f"\nTransaksi untuk pengguna: {user}")
                            transaksi = data["transaksi"]
                            if transaksi:
                                for tanggal, details in transaksi.items():
                                    print(f"Tanggal: {tanggal}, Deskripsi: {details['deskripsi']}, Jumlah: {details['jumlah']}")

                    elif pilihan_admin == 3:
                        tanggal_lama = input("Masukkan tanggal transaksi yang ingin diubah [DD/MM/YYYY]: ")
                        if tanggal_lama in pengguna[username]["transaksi"]:
                            tanggal_baru = input("Masukkan tanggal baru [DD/MM/YYYY]: ")
                            deskripsi_baru = input("Masukkan deskripsi baru: ")
                            jumlah_baru = int(input("Masukkan jumlah baru ('+' untuk pemasukan, '-' untuk pengeluaran): "))
                            pengguna[username]["transaksi"].pop(tanggal_lama)  
                            pengguna[username]["transaksi"][tanggal_baru] = {"deskripsi": deskripsi_baru, "jumlah": jumlah_baru}
                            print("Transaksi berhasil diubah!")
                        else:
                            print("Transaksi dengan tanggal tersebut tidak ditemukan.")

                    elif pilihan_admin == 4:
                        tanggal_hapus = input("Masukkan tanggal transaksi yang ingin dihapus: ")
                        transaksi_dihapus = pengguna[username]["transaksi"].pop(tanggal_hapus, None)
                        if transaksi_dihapus:
                            print(f"Transaksi pada tanggal {tanggal_hapus} berhasil dihapus.")
                        else:
                            print(f"Tidak ada transaksi pada tanggal {tanggal_hapus}.")

                    elif pilihan_admin == 5:
                        print("Terima kasih telah mengakses jurnal keuangan.")
                        break

                    else:
                        print("Opsi tidak valid.")

            else:
                print(f"Login berhasil! Selamat datang, {username}.")
                print(
                    """
                    =================================
                    |             MENU              |
                    =================================
                    |    1. Tambah Transaksi        |           
                    |    2. Tampilkan Transaksi     |    
                    |    3. Ubah Transaksi          |     
                    |    4. Hapus Transaksi         |
                    |    5. Keluar                  |        
                    =================================
                    """
                )

                while True:
                    pilihan_user = int(input("Pilih opsi: "))

                    if pilihan_user == 1:
                        tanggal = input("Masukkan tanggal (DD/MM/YYYY): ")
                        deskripsi = input("Masukkan deskripsi transaksi: ")
                        jumlah = int(input("Masukkan jumlah ('+' untuk pemasukan, '-' untuk pengeluaran): "))
                        pengguna[username]["transaksi"][tanggal] = {"deskripsi": deskripsi, "jumlah": jumlah}
                        print("Transaksi berhasil ditambahkan!")

                    elif pilihan_user == 2:
                        print(f"Transaksi {username}:")
                        if pengguna[username]["transaksi"]:
                            for tanggal, transaksi in pengguna[username]["transaksi"].items():
                                print(f"Tanggal: {tanggal}, Deskripsi: {transaksi['deskripsi']}, Jumlah: {transaksi['jumlah']}")
                        else:
                            print("Tidak ada transaksi.")

                    elif pilihan_user == 3:
                        tanggal_lama = input("Masukkan tanggal transaksi yang ingin diubah: ")
                        if tanggal_lama in pengguna[username]["transaksi"]:
                            tanggal_baru = input("Masukkan tanggal baru (DD/MM/YYYY): ")
                            deskripsi_baru = input("Masukkan deskripsi baru: ")
                            jumlah_baru = int(input("Masukkan jumlah baru ('+' untuk pemasukan, '-' untuk pengeluaran): "))
                            pengguna[username]["transaksi"].pop(tanggal_lama)  
                            pengguna[username]["transaksi"][tanggal_baru] = {"deskripsi": deskripsi_baru, "jumlah": jumlah_baru}
                            print("Transaksi berhasil diubah!")
                        else:
                            print(f"Tidak ada transaksi pada tanggal {tanggal_lama}.")

                    elif pilihan_user == 4:
                        tanggal_hapus = input("Masukkan tanggal transaksi yang ingin dihapus: ")
                        transaksi_dihapus = pengguna[username]["transaksi"].pop(tanggal_hapus, None)
                        if transaksi_dihapus:
                            print(f"Transaksi pada tanggal {tanggal_hapus} berhasil dihapus.")
                        else:
                            print(f"Tidak ada transaksi pada tanggal {tanggal_hapus}.")

                    elif pilihan_user == 5:
                        print("Terima kasih telah menggunakan Jurnal Keuangan.")
                        break

                    else:
                        print("Opsi tidak valid.")
        else:
            print("Error: Username atau password salah.")

    elif pilihan == 3:
        print("Terima kasih telah menggunakan Jurnal Keuangan.")
        break

    else:
        print("Opsi tidak valid.")
