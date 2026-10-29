# Pertemuan 13 - Debugging dan Testing

**Nama:** Keyla Maharani  
**NIM:** 2225250083  
**Kelas:** E  
**Mata Kuliah:** Algoritma dan Pemrograman

## 1. Kasus

Praktik ini membahas proses debugging dan testing pada program Python. Pengujian dilakukan untuk menemukan kesalahan logika, memperbaiki kode, dan memastikan program menghasilkan output yang sesuai dengan harapan.

Program yang diuji meliputi:
1. `kasus/kasus_01_batas_kelulusan.py` untuk menentukan status kelulusan berdasarkan nilai.
2. `kasus/kasus_02_rata_rata.py` untuk menghitung rata-rata nilai.
3. `kasus/kasus_03_file_nilai.py` untuk menangani pembacaan file nilai.
4. `latihan/01_trace_loop.py` untuk menelusuri proses perulangan.
5. `latihan/02_trace_fungsi.py` untuk memahami alur pemanggilan fungsi.
6. `latihan/03_test_case.py` untuk menguji beberapa kondisi kelulusan.
7. `latihan/04_debug_breakpoint.py` untuk memeriksa proses program menggunakan breakpoint.
8. `praktik/praktik_4_debugging.py` untuk menguji dan memperbaiki beberapa kesalahan logika dalam satu program.

## 2. Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| TC01 | Nilai 60 | Lulus | Tidak lulus | Gagal |
| TC02 | Nilai `[80, 90, 70]` | Rata-rata 80.0 | 48.0 | Gagal |
| TC03 | File `nilai.txt` tidak tersedia | Program menangani file yang tidak ditemukan | FileNotFoundError | Gagal |
| TC04 | Data `[80, 60, 90, 70]` | Rata-rata 75.0 | 60.0 | Gagal |
| TC05 | Data `[100, 80]` | Rata-rata 90.0 | 36.0 | Gagal |
| TC06 | Nilai 60 | Lulus | Tidak lulus | Gagal |
| TC07 | Nilai 59 | Tidak lulus | Tidak lulus | Lulus |
| TC08 | Data `[80, 60, 90, 70]` | Nilai tertinggi 90 | 0 | Gagal |
| TC09 | Data kosong `[]` | Program menangani data kosong tanpa pembagian dengan nol | Berpotensi terjadi kesalahan pembagian | Perlu diperbaiki |

## 3. Bug Report

### Bug 1: Kesalahan Batas Kelulusan
- **Gejala:** Nilai 60 dinyatakan tidak lulus.
- **Lokasi:** `kasus/kasus_01_batas_kelulusan.py`.
- **Akar penyebab:** Kondisi menggunakan operator `>` sehingga nilai yang tepat 60 tidak memenuhi syarat.
- **Perbaikan:** Mengganti kondisi menjadi `>= 60`.

### Bug 2: Kesalahan Perhitungan Rata-rata
- **Gejala:** Hasil rata-rata tidak sesuai dengan jumlah data yang dimasukkan.
- **Lokasi:** `kasus/kasus_02_rata_rata.py` dan fungsi `hitung_rata_rata()` pada `praktik/praktik_4_debugging.py`.
- **Akar penyebab:** Program membagi total nilai dengan angka tetap, yaitu 5.
- **Perbaikan:** Menggunakan `len(nilai)` sebagai pembagi dan memeriksa apakah list kosong sebelum melakukan pembagian.

### Bug 3: File Nilai Tidak Ditemukan
- **Gejala:** Program berhenti ketika file `nilai.txt` tidak tersedia.
- **Lokasi:** `kasus/kasus_03_file_nilai.py`.
- **Akar penyebab:** Program belum menangani kondisi file yang tidak ditemukan.
- **Perbaikan:** Menggunakan `try-except` untuk menangani `FileNotFoundError` sehingga program dapat memberikan pesan yang sesuai.

### Bug 4: Kesalahan Menentukan Nilai Tertinggi
- **Gejala:** Program menghasilkan nilai tertinggi 0 meskipun data memiliki nilai lebih besar dari 0.
- **Lokasi:** Fungsi `nilai_tertinggi()` pada `praktik/praktik_4_debugging.py`.
- **Akar penyebab:** Variabel pembanding dimulai dari 0 dan kondisi perbandingan menggunakan operator `<`.
- **Perbaikan:** Menginisialisasi nilai tertinggi dengan elemen pertama list dan menggunakan operator `>` untuk mencari nilai terbesar. Program juga memeriksa data kosong.

## 4. Retest

Setelah perbaikan, program `praktik/praktik_4_debugging.py` dijalankan kembali menggunakan beberapa test case.

| ID | Input | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|---|
| RT01 | `[80, 60, 90, 70]` | Rata-rata 75.0 | 75.0 | Lulus |
| RT02 | `[100, 80]` | Rata-rata 90.0 | 90.0 | Lulus |
| RT03 | Nilai 60 | Lulus | Lulus | Lulus |
| RT04 | Nilai 59 | Tidak lulus | Tidak lulus | Lulus |
| RT05 | `[80, 60, 90, 70]` | Nilai tertinggi 90 | 90 | Lulus |
| RT06 | List kosong `[]` | Tidak terjadi pembagian dengan nol | None | Lulus |

**Hasil pengujian:** Seluruh test case pada program praktik utama berhasil setelah perbaikan. Program dapat menghitung rata-rata berdasarkan jumlah data, menentukan status kelulusan dengan benar, mencari nilai tertinggi, dan menangani list kosong.

## 5. Cara Menjalankan

Pastikan terminal berada di folder utama proyek `pertemuan-13-debugging-2225250083`, kemudian jalankan perintah berikut:

```bash
python praktik/praktik_4_debugging.py
```

Output yang diharapkan:

```text
T1 Rata-rata: 75.0
T2 Rata-rata: 90.0
T3 Status 60: Lulus
T4 Status 59: Tidak lulus
T5 Tertinggi: 90
T6 Data kosong: None
```

## 6. Teknik Debugging

Teknik debugging yang digunakan dalam praktik ini meliputi:
1. **Traceback:** Membaca pesan kesalahan untuk mengetahui lokasi dan jenis kesalahan.
2. **Tracing:** Menelusuri perubahan nilai variabel dan alur perulangan.
3. **Breakpoint:** Menghentikan sementara program untuk memeriksa nilai variabel.
4. **Testing:** Menguji program menggunakan berbagai input, termasuk nilai batas dan data kosong.
5. **Retesting:** Menjalankan kembali test case setelah kode diperbaiki untuk memastikan kesalahan tidak muncul lagi.

## 7. Refleksi

Teknik debugging yang paling membantu adalah testing menggunakan berbagai test case dan memeriksa nilai variabel melalui breakpoint. Testing membantu menemukan kesalahan pada nilai batas kelulusan, perhitungan rata-rata, dan pencarian nilai tertinggi. Sementara itu, breakpoint membantu memahami perubahan nilai variabel selama program dijalankan.

Dari praktik ini, saya memahami bahwa program yang tidak menghasilkan pesan error belum tentu benar. Oleh karena itu, pengujian perlu dilakukan dengan berbagai kondisi input. Setelah kesalahan diperbaiki, program harus diuji kembali agar hasilnya sesuai dengan yang diharapkan.

