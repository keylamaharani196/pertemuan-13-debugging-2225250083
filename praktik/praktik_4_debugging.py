def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return None
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]

    for x in nilai:
        if x > tertinggi:
            tertinggi = x

    return tertinggi


print("T1 Rata-rata:", hitung_rata_rata([80, 60, 90, 70]))
print("T2 Rata-rata:", hitung_rata_rata([100, 80]))
print("T3 Status 60:", status(60))
print("T4 Status 59:", status(59))
print("T5 Tertinggi:", nilai_tertinggi([80, 60, 90, 70]))
print("T6 Data kosong:", hitung_rata_rata([]))
