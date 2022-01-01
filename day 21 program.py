print("data string")
#mencari indeks dalam satu karakter di data list menggunakan metode find()
nama="nurul inayah"
hasil = nama.find('y')
print(hasil)
#cara mengetahui karakter apa yang terdapat dlm indek tertentu
nama = "nurul inayah"
apa=nama[3]
print(apa)
#penyusunan string dapat di akses melalui indeksnya
for i in range(0,12):
    print('nama[%d] : %s ' % (i, nama[i]))
#mengambil karakter
nama="nurul inayah"
hasil=nama[:6]
print(hasil)
nama="nurul inayah"
hasil=nama.upper()#untuk mengganti huruf kecil menjadi huruf kapital
print(hasil)
nama="nurul inayah"
hasil=nama.lower()#untuk mengganti huruf kapital menjadi huruf kecil
print(hasil)






