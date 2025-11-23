# Praktikum5
Penjelasan Program
Dictionary Utama: data_mahasiswa adalah dictionary dengan key sebagai NIM (string) dan value sebagai dictionary berisi detail mahasiswa (nama, tugas, uts, uas, nilai_akhir).
Fungsi hitung_nilai_akhir: Menghitung nilai akhir berdasarkan rumus (tugas * 0.3) + (uts * 0.35) + (uas * 0.35).
Menu Pilihan:
Tambah Data: Meminta input NIM, nama, dan nilai. NIM harus unik. Menghitung nilai akhir dan menyimpan ke dictionary.
Ubah Data: Mencari berdasarkan NIM, lalu memungkinkan update sebagian data. Nilai akhir dihitung ulang.
Hapus Data: Menghapus entry berdasarkan NIM.
Tampilkan Data: Menampilkan semua data dalam format tabel.
Cari Data: Mencari dan menampilkan detail berdasarkan NIM.
Loop Menu: Program berjalan dalam loop hingga user memilih keluar.
Validasi: NIM harus unik saat tambah. Input nilai diasumsikan valid (0-100), tapi bisa ditambahkan validasi lebih lanjut jika diperlukan.

FLOWCHART
          ┌────────────────────┐
          │    Mulai Program   │
          └─────────┬──────────┘
                    │
            ┌───────▼────────┐
            │  Tampilkan Menu │
            └───────┬────────┘
                    │
        ┌───────────┴───────────────────────────┐
        │                                         │
 ┌──────▼──────┐ ┌──────▼──────┐ ┌──────▼──────┐
 │  Tambah Data │ │  Ubah Data  │ │ Hapus Data  │
 └──────────────┘ └─────────────┘ └─────────────┘
        │                │               │
      (simpan)         (update)       (hapus)
        │                │               │
        └──────────┬─────┴──────────────┘
                   │
         ┌─────────▼────────┐
         │ Tampilkan Data    │
         └─────────┬────────┘
                   │
         ┌─────────▼────────┐
         │  Cari Data        │
         └─────────┬────────┘
                   │
         ┌─────────▼────────┐
         │  Keluar?          │─No─┐
         └─────────┬────────┘    │
                   │Yes           │
                   ▼              │
            ┌──────────────┐      │
            │  Program Selesai │◄──┘
            └──────────────┘

  
