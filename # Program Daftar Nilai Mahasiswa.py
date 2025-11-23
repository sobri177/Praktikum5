# Program Daftar Nilai Mahasiswa
# Menggunakan dictionary untuk menyimpan data mahasiswa

data_mahasiswa = {}  # Dictionary utama: key = NIM, value = dict berisi nama, tugas, uts, uas, nilai_akhir

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

def tambah_data():
    nim = input("Masukkan NIM: ")
    if nim in data_mahasiswa:
        print("NIM sudah ada!")
        return
    nama = input("Masukkan Nama: ")
    tugas = float(input("Masukkan Nilai Tugas (0-100): "))
    uts = float(input("Masukkan Nilai UTS (0-100): "))
    uas = float(input("Masukkan Nilai UAS (0-100): "))
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data_mahasiswa[nim] = {
        'nama': nama,
        'tugas': tugas,
        'uts': uts,
        'uas': uas,
        'nilai_akhir': nilai_akhir
    }
    print("Data berhasil ditambahkan!")

def ubah_data():
    nim = input("Masukkan NIM yang ingin diubah: ")
    if nim not in data_mahasiswa:
        print("NIM tidak ditemukan!")
        return
    print("Data lama:", data_mahasiswa[nim])
    nama = input("Masukkan Nama baru (kosongkan jika tidak diubah): ")
    tugas = input("Masukkan Nilai Tugas baru (kosongkan jika tidak diubah): ")
    uts = input("Masukkan Nilai UTS baru (kosongkan jika tidak diubah): ")
    uas = input("Masukkan Nilai UAS baru (kosongkan jika tidak diubah): ")
    
    if nama:
        data_mahasiswa[nim]['nama'] = nama
    if tugas:
        data_mahasiswa[nim]['tugas'] = float(tugas)
    if uts:
        data_mahasiswa[nim]['uts'] = float(uts)
    if uas:
        data_mahasiswa[nim]['uas'] = float(uas)
    
    # Hitung ulang nilai akhir
    data_mahasiswa[nim]['nilai_akhir'] = hitung_nilai_akhir(
        data_mahasiswa[nim]['tugas'],
        data_mahasiswa[nim]['uts'],
        data_mahasiswa[nim]['uas']
    )
    print("Data berhasil diubah!")

def hapus_data():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus!")
    else:
        print("NIM tidak ditemukan!")

def tampilkan_data():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa.")
        return
    print("Daftar Nilai Mahasiswa:")
    print("NIM\t\tNama\t\tTugas\tUTS\tUAS\tNilai Akhir")
    for nim, info in data_mahasiswa.items():
        print(f"{nim}\t{info['nama']}\t{info['tugas']}\t{info['uts']}\t{info['uas']}\t{info['nilai_akhir']:.2f}")

def cari_data():
    nim = input("Masukkan NIM yang dicari: ")
    if nim in data_mahasiswa:
        info = data_mahasiswa[nim]
        print(f"NIM: {nim}")
        print(f"Nama: {info['nama']}")
        print(f"Tugas: {info['tugas']}")
        print(f"UTS: {info['uts']}")
        print(f"UAS: {info['uas']}")
        print(f"Nilai Akhir: {info['nilai_akhir']:.2f}")
    else:
        print("NIM tidak ditemukan!")

# Menu utama
while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        ubah_data()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '4':
        tampilkan_data()
    elif pilihan == '5':
        cari_data()
    elif pilihan == '6':
        break
    else:
        print("Pilihan tidak valid!")
