def hitung_total(data):
    total = 0

    for nilai in data:
        total += nilai

    return total


nilai = [80, 60, 90, 70]
hasil = hitung_total(nilai)

print("Total nilai:", hasil)
