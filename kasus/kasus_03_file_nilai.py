def baca_nilai(nama_file):
    try:
        with open(nama_file, "r") as file:
            nilai = file.readlines()
        return nilai
    except FileNotFoundError:
        print("File nilai tidak ditemukan.")
        return []


print(baca_nilai("nilai.txt"))
