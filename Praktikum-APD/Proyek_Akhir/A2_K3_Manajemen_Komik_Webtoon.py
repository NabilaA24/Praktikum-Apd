from prettytable import PrettyTable

#MENYIMPAN DATA ADMIN DENGAN TUPLE
admin = ('admin')  
#MENYIMPAN DATA USERS DENGAN DICTIONARY
users = {} 
#DATA KOMIK WEBTOON YANG TERSEDIA
komik_webtoon = {
'Iblis di Antara Kita' : {'jumlah pembaca' : '12,1 Juta', 'rating' : '9,58', 'genre' : 'Thriller', 'tahun terbit' : '2023'},
'Kemala' : {'jumlah pembaca' : '21,6 Juta', 'rating' : '9,91', 'genre' : 'Horor', 'tahun terbit' : '2020'},
'The Gwichon Village Mystery' : {'jumlah pembaca' : '4,3 Juta', 'rating' : '9,88', 'genre' : 'Thriller', 'tahun terbit' : '2024'},
'Deadly 7 Inside Me' : {'jumlah pembaca' : '107,4 Juta', 'rating' : '9,88', 'genre' : 'Fantasi', 'tahun terbit' : '2016'},
'Nusantara Droid War' : {'jumlah pembaca' : '127,6 Juta', 'rating' : '9,77', 'genre' : 'Fantasi', 'tahun terbit' : '2015'},
'Hand Jumper' : {'jumlah pembaca' : '35,5 Juta', 'rating' : '9,84', 'genre' : 'Thriller', 'tahun terbit' : '2022'},
'Orange Marmalade' : {'jumlah pembaca' : '128,8 Juta', 'rating' : '9,67', 'genre' : 'Romance', 'tahun terbit' : '2014'},
'Untouchable' : {'jumlah pembaca' : '173,1 Juta', 'rating' : '9,68', 'genre' : 'Romance', 'tahun terbit' : '2014'},
'Unholy Blood' : {'jumlah pembaca' : '131,1 Juta', 'rating' : '9,85', 'genre' : 'Supernatural', 'tahun terbit' : '2020'},
'lazy cooking' : {'jumlah pembaca' : '142,4 Juta', 'rating' : '9,70', 'genre' : 'Slice of Life', 'tahun terbit' : '2016'},
'WEE!!!' : {'jumlah pembaca' : '426,1 Juta', 'rating' : '9,75', 'genre' : 'Comedy', 'tahun terbit' : '2016'},
'Pasutri Gaje' : {'jumlah pembaca' : '910,7 Juta', 'rating' : '9,77', 'genre' : 'Romance', 'tahun terbit' : '2016'},
'GOOD/BAD FORTUNE' : {'jumlah pembaca' : '147,7 Juta', 'rating' : '9,85', 'genre' : 'Drama', 'tahun terbit' : '2018'},
'Who is Mr. President?' : {'jumlah pembaca' : '44,2 Juta', 'rating' : '9,91', 'genre' : 'Drama', 'tahun terbit' : '2021'}
}

#MENYIMPAN DATA WEBTOON FAVORITE USERS
favorite_user = {} 

#FUNGSI MENAMPILKAN MENU UTAMA 
def menu_utama():
    while True:
        #DAFTAR PILIHAN MENU UTAMA
        print("""\033[95m
        =======================================================
        | Selamat Datang di Manajemen Data Webtoon Indonesia  |
        |               Silahkan Registrasi!                  |
        |                   1. Registrasi                     |
        |                   2. Login                          |
        |                   3. Exit                           |
        =======================================================
        \033[0m""")
        #ERROR HANDLING
        try:
            #INPUT PILIHAN MENU UTAMA
            pilihan = int(input("Masukkan pilihan anda: "))
            if pilihan == 1:
                registrasi()
            elif pilihan == 2:
                login()
            elif pilihan == 3:
                end_data()
            #PILIHAN DILUAR DARI MENU UTAMA
            else:
                print("==================================")
                print("\033[91mPilihan tidak valid\033[0m")
        #ERROR JIKA INPUT PILIHAN BUKAN INTEGER
        except ValueError:
            print("==================================")
            print("\033[91mInput yang dimasukkan tidak valid\033[0m")

#FUNGSI REGISTRASI
def registrasi():
    #ERROR HANDLING
    try:
        #INPUT USERNAME
        username = str(input("Buat username: "))
        #INPUT PASSWORD
        password = str(input("Buat password: "))
        #CEK USERNAME SUDAH DIGUNAKAN ATAU TIDAK
        if username in users:
            print("\033[91mError: Username sudah digunakan\033[0m")
        elif username == admin and password == admin:
            print("\033[91mError: Username sudah digunakan\033[0m")
        else:
            #MENAMBAHKAN USER KEDALAM VARIABEL
            users[username] =  password
            print("Pendaftaran berhasil!")
    #ERROR JIKA INPUT BUKAN STRING
    except ValueError:
        print("\033[91minputan tidak valid\033[0m")
        registrasi()

#FUNGSI LOGIN
def login():
    #ERROR HANDLING
    try:
        #INPUT USERNAME
        username = str(input("Masukkan username: "))
        #INPUT PASSSWORD
        password = str(input("Masukkan password: "))
        #USERNAME DAN PASSWORD ADALAH USER BIASA
        if username in users and password == users[username]:
            print("Login berhasil!")
            menu_user(username)
        #USERNAME DAN PASSSWORD ADALAH ADMIN
        elif username == admin and password == admin:
            print("Login Berhasil!")
            menu_admin()
        #OUTPUT JIKA INPUT USERNAME ATAU PASSWORD SALAH
        else:
            print("\033[91mUsername atau password salah.\033[0m")
    #ERROR JIKA INPUT BUKAN STRING
    except ValueError:
        print("\033[91mInputan tidak valid\033[0m")
        login()

#FUNGSI MENAMBAH DATA
def tambah_data():
    #ERROR HANDLING
    try:
        #INPUT JUDUL WEBTOON
        judul_webtoon = str(input('Judul Webtoon: '))
        #MENYIMPAN DATA WEBTOON YANG BARU DITAMBAHKAN
        komik_webtoon[judul_webtoon] = {}
        #INPUT JUMLAH PEMBACA
        komik_webtoon[judul_webtoon]['jumlah pembaca'] = str(input('Jumlah Pembaca: '))
        #INPUT RATING 
        komik_webtoon[judul_webtoon]['rating'] = float(input('Rating: '))
        #INPUT GENRE
        komik_webtoon[judul_webtoon]['genre'] = str(input('Genre: '))
        #INPUT TAHUN TERBIT
        komik_webtoon[judul_webtoon]['tahun terbit'] = int(input('Tahun Terbit: '))
        #OUTPUT JIKA DATA BERHASIL DIATMBAHKAN
        print(f"Data berhasil ditambahkan.")
    #ERROR JIKA INPUT TIDAK SESUAI
    except ValueError:
        print("\033[91mInput Anda tidak valid!\033[0m")
        tambah_data()

#FUNGSI MENAMPILKAN MENU USER BIASA
def menu_user(username):
    while True: 
        print("""\033[96m
        ===================================================
        [      MANAJEMEN DATA KOMIK WEBTOON INDONESIA     ]
        ===================================================
        [1. TAMPILKAN DATA                                ]
        [2. TAMBAH FAVORITE                               ]
        [3. TAMPILKAN KOMIK FAVORITE                      ]
        [4. HAPUS KOMIK DARI FAVORITE                     ]
        [5. EXIT                                          ]
        ===================================================
        \033[0m""")
        try :
            pilihan = int(input("PILIH: "))
            if pilihan == 1:
                tampil_data()
            elif pilihan == 2:
                tambah_favorite(username)
            elif pilihan == 3:
                buka_favorite(username)
            elif pilihan == 4:
                hapus_favorite(username)
            elif pilihan == 5:
                menu_utama()
            else:
                print("\033[91mPilihan tidak valid. Pilih angka 1/2/3/4/5.\033[0m")
        except ValueError :
                print("\033[91mPilihan tidak valid.\033[0m")
                menu_user(username)

#FUNGSI MENAMPILKAN MENU ADMIN
def menu_admin():
    #PERULANGAN UNTUK MENAMPILKAN MENU ADMIN
    while True:
        print("""\033[96m
        ================================================
        [                    MENU                      ]
        ================================================
        [1. TAMBAH WEBTOON                             ]           
        [2. TAMPILKAN DATA WEBTOON                     ]    
        [3. TAMPILKAN USER                             ]     
        [4. UPDATE DATA WEBTOON                        ]
        [5. HAPUS WEBTOON                              ]
        [6. EXIT                                       ]
        ================================================
        \033[0m""")
        try:  
            pilihan = int(input("PILIH: "))
            if pilihan == 1:
                tambah_data()
            elif pilihan == 2:
                tampil_data()
            elif pilihan == 3:
                tampilkan_user()
            elif pilihan == 4:
                update_data()
            elif pilihan == 5:
                hapus_komik()
            elif pilihan == 6:
                menu_utama()
            else:
                print("\033[91mPilihan tidak valid. Pilih angka 1/2/3/4/5/6.\033[0m")
        except ValueError:
            print("\033[91mInputan tidak valid\033[0m")

#FUNGSI MENAMPILKAN DATA
def tampil_data():
    #ERROR HANDLING
    try:
        komik_table = PrettyTable()
        komik_table.field_names = ['No', 'Judul Webtoon', 'Jumlah Pembaca', 'Rating', 'Genre', 'Tahun Terbit']
        nomor = 1
        for judul_komik, data_komik in komik_webtoon.items():
            komik_table.add_row([
                nomor,
                judul_komik,
                data_komik['jumlah pembaca'],
                data_komik['rating'],
                data_komik['genre'],
                data_komik['tahun terbit']
            ])
            nomor += 1
        print("Daftar Webtoon:")
        print(komik_table)
    #OUTPUT JIKA DATA BELUM ADA
    except ValueError:
        print("================================")
        print("\033[91mTidak ada data untuk ditampilkan atau terjadi kesalahan.\033[0m")

#FUNGSI MENAMPILKAN DAFTAR USER YANG TERDAFTAR DALAM PROGRAM
def tampilkan_user():
    if not users:
        print("\033[91mDaftar Username kosong\033[0m")
    else :
        users_table = PrettyTable()
        users_table.field_names = ["No", "Username"]
        nomor = 1 
        for username in users:
            users_table.add_row([nomor, username])
            nomor += 1
        print("Daftar Users: ")
        print(users_table)

#FUNGSI MENGUPDATE DATA KOMIK
def update_data():
    tampil_data()
    judul_lama = input("Judul Webtoon lama: ")
    if judul_lama in komik_webtoon:
        pembaca_baru = str(input("Masukkan jumlah pembaca baru: "))
        genre_baru = str(input("Masukkan genre baru: "))
        rating_baru = float(input("Masukkan rating baru: "))
        terbit_baru = int(input("Masukkan tahun terbit baru: "))
        komik_webtoon[judul_lama] = {
            'jumlah pembaca': pembaca_baru,
            'genre': genre_baru,
            'rating': rating_baru,
            'tahun terbit' : terbit_baru
        }
        print(f"Data {judul_lama} berhasil diubah.")
    else:
        print("\033[91mData tidak valid.\033[0m")
        update_data()

#FUNGSI MENGHAPUS KOMIK 
def hapus_komik():
    judul = input("Masukkan judul komik yang ingin dihapus: ")
    if judul in komik_webtoon:
        del komik_webtoon[judul]
        print(f"Data komik '{judul}' berhasil dihapus.")
    else:
        print("\033[91mKomik tidak ditemukan.\033[0m")
        hapus_komik()

# FUNGSI MENAMBAHKAN DAFTAR FAVORITE USER
def tambah_favorite(username):
    if username not in favorite_user:
        favorite_user[username] = {}  
    tampil_data()
    print("===================================")
    try:
        judul_webtoon = str(input("Judul webtoon yang ingin ditambahkan ke favorite: "))
        if judul_webtoon in komik_webtoon:
            favorite_user[username][judul_webtoon] = komik_webtoon[judul_webtoon]
            print(f"'{judul_webtoon}' berhasil ditambahkan ke favorit!")
        else:
            print("\033[91mWebtoon tidak ada dalam daftar\033[0m")
            tambah_favorite(username)
    except ValueError:
        print("\033[91mInput yang dimasukkan tidak valid.\033[0m")
        tambah_favorite(username)

# FUNGSI MENAMPILKAN DAFTAR FAVORITE USER
def buka_favorite(username):
    if username not in favorite_user or not favorite_user[username]:
        print("\033[91mWebtoon Favorite Kosong\033[0m")
        menu_user(username)
    else:
        komik_table = PrettyTable()
        komik_table.field_names = ["No", "Judul Webtoon", "Jumlah Pembaca", "Rating", "Genre", "Tahun Terbit"]
        nomor = 1
        for judul_komik, data_komik in favorite_user[username].items():
            komik_table.add_row([
                nomor,
                judul_komik,
                data_komik["jumlah pembaca"],
                data_komik["rating"],
                data_komik["genre"],
                data_komik["tahun terbit"]
            ])
            nomor += 1
        print("Daftar Webtoon Favorit:")
        print(komik_table)

# FUNGSI MENGHAPUS WEBTOON FAVORITE DARI DAFTAR FAVORIT
def hapus_favorite(username):
    buka_favorite(username)
    try :
        judul_webtoon = str(input("Judul Webtoon yang ingin dihapus : "))
        if judul_webtoon in favorite_user[username] :
            del favorite_user[username][judul_webtoon]
            print(f"Komik Webtoon '{judul_webtoon}' berhasil dihapus dari favorite.")
        else :
            print("\033[91mJudul webtoon tidak ada dalam daftar favorite.\033[0m")
            hapus_favorite(username)
    except ValueError :
        print("\033[94mInput yang dimasukkan tidak valid.\033[0m")
        hapus_favorite(username)

# FUNGSI MENUTUP PROGRAN
def end_data():
    print("\033[94mTerima kasih telah mengunjungi Manajemen Data Komik Webtoon Indonesia\033[0m")    
    exit()
    

# Start the program
menu_utama()



