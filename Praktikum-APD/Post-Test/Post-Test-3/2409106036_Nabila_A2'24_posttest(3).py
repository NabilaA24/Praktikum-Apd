Nama = input("masukkan nama anda: ")
NIM = input("masukkan NIM anda: ")

Jumlah_pinjaman = int(input("masukkan jumlah pinjaman: "))
Lama_Cicilan = int(input("masukkan lama cicilan: "))

if Lama_Cicilan == 1:
    Jumlah_Bulan = 12
    Bunga_pertahun = 0.07
elif Lama_Cicilan == 2:
    Bunga_pertahun = 0.13
    Jumlah_Bulan = 24
elif Lama_Cicilan == 3:
    Bunga_pertahun = 0.19
    Jumlah_Bulan = 36
else:
    print("tidak valid")

Bunga_perbulan = (Bunga_pertahun/12)*Jumlah_pinjaman
Total_cicilan_perbulan = (Jumlah_pinjaman+Bunga_perbulan) / Jumlah_Bulan

print(
    "Atas nama " + Nama + " dengan NIM " + NIM + " memiliki pinjaman sebesar " + str(int(Jumlah_pinjaman)) + "\n"
    "dengan bunga per bulan sebesar Rp " + str(int(Bunga_perbulan)) + "\n"
    "total cicilan per bulan yang harus dibayar sebesar Rp " + str(int(Total_cicilan_perbulan))
    )