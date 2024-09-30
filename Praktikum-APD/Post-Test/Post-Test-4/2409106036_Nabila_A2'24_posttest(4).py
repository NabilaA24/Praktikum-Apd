attempts = 0

while (attempts < 3):
    username = input("masukkan username anda: ")
    password = input("masukkan password anda: ")   
    if username == "nabila" and password == "36":
        print("Berhasil")
        Jumlah_pinjaman = int(input("masukkan jumlah pinjamanan: "))
        Lama_Cicilan = int(input("masukkan lama pinjaman: "))
        if Lama_Cicilan == 1:
            Bunga_pertahun = 0.07
            Jumlah_Bulan = 12
        elif Lama_Cicilan == 2:
            Bunga_pertahun = 0.13
            Jumlah_Bulan = 24
        elif Lama_Cicilan == 3:
            Bunga_pertahun = 0.19
            Jumlah_Bulan = 36
        else:
            print("tidak valid")
        Bunga_perbulan = (Bunga_pertahun/12)*Jumlah_pinjaman
        Total_cicilan_perbulan = (Jumlah_pinjaman+Bunga_perbulan) /Jumlah_Bulan
        print(
        "Atas nama " + username + " dengan NIM 24091060" + password + " memiliki pinjaman sebesar " + str(int(Jumlah_pinjaman)) + "\n"
        "dengan bunga per bulan sebesar Rp " + str(int(Bunga_perbulan)) + "\n"
        "total cicilan per bulan yang harus dibayar sebesar Rp " + str(int(Total_cicilan_perbulan))
        )
        Pemberhentian = str(input("Apakah anda ingin berhenti? [Y/N]: "))
        if Pemberhentian == "Y":
            break
    else:
        attempts += 1
        print("gagal")
else:
    print("Silahkan coba lagi beberapa saat nanti")




