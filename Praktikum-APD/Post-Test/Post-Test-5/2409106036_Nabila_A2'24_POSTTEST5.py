print(
    """
Selamat datang di Jurnal Keuangan!"
===========================
|   SILAHKAN PILIH OPSI   |
===========================
|    1. REGISTER          |           
|    2. LOGIN             |          
|    3. EXIT              |       
===========================
"""
)

pengguna = [
    ["nabila", "036", []], 
]

while True:
        pilihan = int(input("Pilih opsi: "))

        if pilihan == 1:
            username = input("Buat username: ")
            password = input("Buat password: ")
            username_ada = False
            for user in pengguna:
                if user[0] == username:
                    username_ada = True
                    break

            if username_ada:
                print("Error: Username sudah digunakan")
            else:
                pengguna.append([username, password, []])
                print("Pendaftaran berhasil!")

        elif pilihan == 2:
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            user_data = None
            for i in range(len(pengguna)):
                if pengguna[i][0] == username and pengguna[i][1] == password:
                    user_data = i
                    break

            if user_data is not None:
                if username == "nabila":
                    print(
                    """"
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
                            pengguna[user_data][2].append([tanggal, deskripsi, jumlah])
                            print("Transaksi Anda berhasil ditambahkan")

                        elif pilihan_admin == 2:
                            print(f"Data pengguna dan transaksi:")
                            for i in range(len(pengguna)):
                                print(f"\n Data Pengguna ke-{i+1}\nNAMA: {pengguna[i][0]}\nPASSWORD: {pengguna[i][1]}\nTRANSAKSI: ")
                                if pengguna[i][2]:
                                    for transaksi in pengguna[i][2]:
                                        print(f"Tanggal: {transaksi[0]}, Deskripsi: {transaksi[1]}, Jumlah: {transaksi[2]}")
                                else:
                                    print("Tidak ada transaksi")

                        elif pilihan_admin == 3:
                            tanggal_lama = input("Masukkan tanggal transaksi yang ingin diubah [DD/MM/YYYY]: ")
                            transaksi_ditemukan = False
                            for i in range(len(pengguna)):
                                for j in range(len(pengguna[i][2])):  
                                    if pengguna[i][2][j][0] == tanggal_lama:  
                                        transaksi_ditemukan = True
                                        print(f"Transaksi ditemukan untuk pengguna {pengguna[i][0]}:")
                                        print(f"Tanggal: {pengguna[i][2][j][0]}, Deskripsi: {pengguna[i][2][j][1]}, Jumlah: {pengguna[i][2][j][2]}")
                                        tanggal_baru = input("Masukkan tanggal baru [DD/MM/YYYY]: ")
                                        deskripsi_baru = input("Masukkan deskripsi baru: ")
                                        jumlah_baru = int(input("Masukkan jumlah baru ('+' untuk pemasukan, '-' untuk pengeluaran): "))
                                        pengguna[i][2][j] = [tanggal_baru, deskripsi_baru, jumlah_baru]
                                        print("Transaksi berhasil diubah.")
                                        break

                                if transaksi_ditemukan:
                                    break

                            if not transaksi_ditemukan:
                                print("Transaksi dengan tanggal tersebut tidak ditemukan.")

                        elif pilihan_admin == 4:
                            nama_pengguna = input("Masukkan nama pengguna yang transaksinya ingin dihapus: ")
                            tanggal_hapus = input("Masukkan tanggal transaksi yang ingin dihapus: ")
                            for i in range(len(pengguna)):
                                if pengguna[i][0] == nama_pengguna:
                                    for j in range(len(pengguna[i][2])):
                                        if pengguna[i][2][j][0] == tanggal_hapus:
                                            del pengguna[i][2][j]
                                            print(f"Transaksi pada tanggal {tanggal_hapus} berhasil dihapus.")
                                            break

                        elif pilihan_admin == 5:
                            print("Terima kasih telah mengakses jurnal keuangan")
                            break

                        else:
                            print("anda salah input")

                else:
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
                            tanggal = input("Masukkan tanggal (DD/MM/YYYY): ")
                            deskripsi = input("Masukkan deskripsi transaksi: ")
                            jumlah = int(input("Masukkan jumlah ('+' untuk pemasukan, '-' untuk pengeluaran): "))
                            pengguna[user_data][2].append([tanggal, deskripsi, jumlah])
                            print("Transaksi anda berhasil ditambahkan")

                        elif pilihan_user == 2:
                            print(f"Transaksi {username}:")
                            if pengguna[user_data][2]:
                                for transaksi in pengguna[user_data][2]:
                                    print(f"Tanggal: {transaksi[0]}, Deskripsi: {transaksi[1]}, Jumlah: {transaksi[2]}")
                            else:
                                print("Tidak ada transaksi.")

                        elif pilihan_user == 3:
                            tanggal_lama = input("Masukkan tanggal transaksi yang ingin diubah: ")
                            for jurnal in pengguna[user_data][2]:
                                if jurnal[0] == tanggal_lama:
                                    tanggal_baru = input("Masukkan tanggal baru (DD/MM/YYYY): ")
                                    deskripsi_baru = input("Masukkan deskripsi baru: ")
                                    jumlah_baru = input("Masukkan jumlah baru: ")
                                    jurnal[0] = tanggal_baru
                                    jurnal[1] = deskripsi_baru
                                    jurnal[2] = jumlah_baru
                                    print("Transaksi berhasil diubah")

                        elif pilihan_user == 4:
                            tanggal_hapus = input("Masukkan tanggal transaksi yang ingin dihapus: ")
                            for i in range(len(pengguna[user_data][2])):
                                if pengguna[user_data][2][i][0] == tanggal_hapus:
                                    del pengguna[user_data][2][i]
                                    print(f"Transaksi pada tanggal {tanggal_hapus} berhasil dihapus.")
                                    break
                            else:
                                print(f"Tidak ada transaksi pada tanggal {tanggal_hapus}.")

                        elif pilihan_user == 5:
                            print("Terima kasih telah menggunakan Jurnal Keuangan")
                            break

                        else:
                            print("Anda salah input")
            else:
                print("Error: Username atau password salah.")
                
        elif pilihan == 3:
            print("Terima kasih telah menggunakan jurnal keuangan ini.")
            break

        else:
            print("Opsi tidak valid")
