def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon


hasil = hitung_diskon(200000, 10)
print("Harga setelah diskon:", hasil)
