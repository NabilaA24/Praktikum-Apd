nama = input("masukkan nama :" )
NIM = input("masukkan NIM :")
harga_beras = int(input("masukkan harga beras :"))

Persentase_Diskon_mawar = 0.11
Persentase_Diskon_sania = 0.14
Persentase_Diskon_maknyus = 0.17

Diskon_Beras_Mawar = harga_beras*Persentase_Diskon_mawar
Diskon_Beras_Sania = harga_beras*Persentase_Diskon_sania
Diskon_Beras_Maknyus = harga_beras*Persentase_Diskon_maknyus

Harga_Diskon_Beras_Mawar = harga_beras - Diskon_Beras_Mawar
Harga_Diskon_Beras_Sania = harga_beras - Diskon_Beras_Sania
Harga_Diskon_Beras_Maknyus = harga_beras - Diskon_Beras_Maknyus

print(
    nama + " dengan NIM " + NIM + " ingin membeli beras seharga Rp" + str(harga_beras) +"\n"
    "Jika dia membeli beras Mawar ia harus membayar " + str(int(Harga_Diskon_Beras_Mawar)) + " Setelah mendapat diskon 11%.\n" 
    "Jika dia membeli beras Sania ia harus membayar " + str(int(Harga_Diskon_Beras_Sania)) + " Setelah mendapat diskon 14%.\n"
    "Jika dia membeli beras Maknyus ia harus membayar " + str(int(Harga_Diskon_Beras_Maknyus)) + " Setelah mendapat diskon 17%."
    )
