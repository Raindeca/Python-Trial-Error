hargaToko = float(input("Masukkan Harga toko: "))
hargaJual = float(input("Masukkan harga Jual: "))

if hargaJual > hargaToko:
    bonus= float(0.05 * hargaJual)
    pesan = "Selamaaaaaaaaaaa!"
    print("Bonus Anda = Rp ", bonus, " ", pesan)
else:
    bonus = 0
    print("Bonus Anda = Rp ", bonus)
