# Kelas untuk mengelola peralatan/inventaris di lab
class InventarisLab:
    def __init__(self):
        self.peralatan = {}

    def tambah_peralatan(self, nama, jumlah):
        if nama in self.peralatan:
            self.peralatan[nama] += jumlah
        else:
            self.peralatan[nama] = jumlah
        print(f"{jumlah} {nama} ditambahkan ke inventaris.")

    def hapus_peralatan(self, nama, jumlah):
        if nama in self.peralatan and self.peralatan[nama] >= jumlah:
            self.peralatan[nama] -= jumlah
            print(f"{jumlah} {nama} dihapus dari inventaris.")
        else:
            print(f"Peralatan {nama} tidak mencukupi atau tidak tersedia.")

    def cek_inventaris(self):
        print("Daftar inventaris lab:")
        for nama, jumlah in self.peralatan.items():
            print(f"- {nama}: {jumlah} unit")


# Kelas untuk mengelola pengguna lab
class PenggunaLab:
    def __init__(self):
        self.pengguna = {}

    def tambah_pengguna(self, nama, role):
        self.pengguna[nama] = role
        print(f"Pengguna {nama} ditambahkan sebagai {role}.")

    def hapus_pengguna(self, nama):
        if nama in self.pengguna:
            del self.pengguna[nama]
            print(f"Pengguna {nama} dihapus dari daftar.")
        else:
            print(f"Pengguna {nama} tidak ditemukan.")

    def daftar_pengguna(self):
        print("Daftar pengguna lab:")
        for nama, role in self.pengguna.items():
            print(f"- {nama}: {role}")


# Kelas untuk mengelola penggunaan lab
class PenggunaanLab:
    def __init__(self):
        self.penggunaan = []

    def tambah_penggunaan(self, pengguna, waktu, kegiatan):
        self.penggunaan.append({
            'pengguna': pengguna,
            'waktu': waktu,
            'kegiatan': kegiatan
        })
        print(f"Penggunaan lab oleh {pengguna} pada {waktu} untuk {kegiatan} ditambahkan.")

    def hapus_penggunaan(self, pengguna, waktu):
        for penggunaan in self.penggunaan:
            if penggunaan['pengguna'] == pengguna and penggunaan['waktu'] == waktu:
                self.penggunaan.remove(penggunaan)
                print(f"Penggunaan lab oleh {pengguna} pada {waktu} dihapus.")
                return
        print(f"Penggunaan oleh {pengguna} pada {waktu} tidak ditemukan.")

    def daftar_penggunaan(self):
        print("Daftar penggunaan lab:")
        for penggunaan in self.penggunaan:
            print(f"- {penggunaan['pengguna']} menggunakan lab pada {penggunaan['waktu']} untuk {penggunaan['kegiatan']}")


# Kelas Manajemen Lab Komputer Utama
class ManajemenLabKomputer:
    def __init__(self):
        self.inventaris = InventarisLab()
        self.pengguna_lab = PenggunaLab()
        self.penggunaan_lab = PenggunaanLab()

    def menu(self):
        while True:
            print("\n=== Sistem Manajemen Lab Komputer ===")
            print("1. Kelola Inventaris Lab")
            print("2. Kelola Pengguna Lab")
            print("3. Kelola Penggunaan Lab")
            print("4. Keluar")
            pilihan = input("Pilih opsi (1-4): ")

            if pilihan == "1":
                self.menu_inventaris()
            elif pilihan == "2":
                self.menu_pengguna()
            elif pilihan == "3":
                self.menu_penggunaan()
            elif pilihan == "4":
                print("Keluar dari sistem manajemen lab.")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

    def menu_inventaris(self):
        while True:
            print("\n=== Kelola Inventaris Lab ===")
            print("1. Tambah Peralatan")
            print("2. Hapus Peralatan")
            print("3. Lihat Daftar Inventaris")
            print("4. Kembali ke menu utama")
            pilihan = input("Pilih opsi (1-4): ")

            if pilihan == "1":
                nama = input("Nama peralatan: ")
                jumlah = int(input("Jumlah: "))
                self.inventaris.tambah_peralatan(nama, jumlah)
            elif pilihan == "2":
                nama = input("Nama peralatan: ")
                jumlah = int(input("Jumlah: "))
                self.inventaris.hapus_peralatan(nama, jumlah)
            elif pilihan == "3":
                self.inventaris.cek_inventaris()
            elif pilihan == "4":
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

    def menu_pengguna(self):
        while True:
            print("\n=== Kelola Pengguna Lab ===")
            print("1. Tambah Pengguna")
            print("2. Hapus Pengguna")
            print("3. Lihat Daftar Pengguna")
            print("4. Kembali ke menu utama")
            pilihan = input("Pilih opsi (1-4): ")

            if pilihan == "1":
                nama = input("Nama pengguna: ")
                role = input("Peran (misal: Mahasiswa, Dosen, Teknisi): ")
                self.pengguna_lab.tambah_pengguna(nama, role)
            elif pilihan == "2":
                nama = input("Nama pengguna: ")
                self.pengguna_lab.hapus_pengguna(nama)
            elif pilihan == "3":
                self.pengguna_lab.daftar_pengguna()
            elif pilihan == "4":
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

    def menu_penggunaan(self):
        while True:
            print("\n=== Kelola Penggunaan Lab ===")
            print("1. Tambah Penggunaan Lab")
            print("2. Hapus Penggunaan Lab")
            print("3. Lihat Daftar Penggunaan Lab")
            print("4. Kembali ke menu utama")
            pilihan = input("Pilih opsi (1-4): ")

            if pilihan == "1":
                pengguna = input("Nama pengguna: ")
                waktu = input("Waktu penggunaan (misal: 10:00-12:00): ")
                kegiatan = input("Kegiatan: ")
                self.penggunaan_lab.tambah_penggunaan(pengguna, waktu, kegiatan)
            elif pilihan == "2":
                pengguna = input("Nama pengguna: ")
                waktu = input("Waktu penggunaan: ")
                self.penggunaan_lab.hapus_penggunaan(pengguna, waktu)
            elif pilihan == "3":
                self.penggunaan_lab.daftar_penggunaan()
            elif pilihan == "4":
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

# Membuat instance dari ManajemenLabKomputer
manajemen_lab = ManajemenLabKomputer()
manajemen_lab.menu()
