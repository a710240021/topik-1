class Mobil:
    def __init__(self, merk, model, tahun_produksi, warna, nomor_polisi, kecepatan_maksimum, bahan_bakar, jumlah_penumpang):
        self.merk = merk
        self.model = model
        self.tahun_produksi = tahun_produksi
        self.warna = warna
        self.nomor_polisi = nomor_polisi
        self.kecepatan_maksimum = kecepatan_maksimum
        self.bahan_bakar = bahan_bakar
        self.jumlah_penumpang = jumlah_penumpang
        self.posisi_gigi = 0  # Netral
        self.status_mesin = False # Mesin mati
        self.kecepatan_sekarang = 0

    def start_engine(self):
        if not self.status_mesin:
            self.status_mesin = True
            print(f"Mesin mobil {self.merk} {self.model} dinyalakan.")
        else:
            print(f"Mesin mobil {self.merk} {self.model} sudah menyala.")

    def stop_engine(self):
        if self.status_mesin:
            self.status_mesin = False
            self.kecepatan_sekarang = 0
            self.posisi_gigi = 0
            print(f"Mesin mobil {self.merk} {self.model} dimatikan.")
        else:
            print(f"Mesin mobil {self.merk} {self.model} sudah mati.")

    def percepat(self, jumlah_kecepatan):
        if self.status_mesin:
            if self.kecepatan_sekarang + jumlah_kecepatan <= self.kecepatan_maksimum:
                self.kecepatan_sekarang += jumlah_kecepatan
                print(f"Mobil {self.merk} {self.model} dipercepat. Kecepatan sekarang: {self.kecepatan_sekarang} km/jam.")
            else:
                self.kecepatan_sekarang = self.kecepatan_maksimum
                print(f"Mobil {self.merk} {self.model} mencapai kecepatan maksimum: {self.kecepatan_sekarang} km/jam.")
        else:
            print(f"Nyalakan mesin mobil {self.merk} {self.model} terlebih dahulu!")

    def perlambat(self, jumlah_kecepatan):
        if self.status_mesin:
            if self.kecepatan_sekarang - jumlah_kecepatan >= 0:
                self.kecepatan_sekarang -= jumlah_kecepatan
                print(f"Mobil {self.merk} {self.model} diperlambat. Kecepatan sekarang: {self.kecepatan_sekarang} km/jam.")
            else:
                self.kecepatan_sekarang = 0
                print(f"Mobil {self.merk} {self.model} berhenti. Kecepatan sekarang: {self.kecepatan_sekarang} km/jam.")
        else:
            print(f"Mesin mobil {self.merk} {self.model} mati.")

    def ganti_gigi(self, gigi_baru):
        if self.status_mesin:
            self.posisi_gigi = gigi_baru
            print(f"Mobil {self.merk} {self.model} berganti gigi ke posisi {self.posisi_gigi}.")
        else:
            print(f"Nyalakan mesin mobil {self.merk} {self.model} terlebih dahulu untuk ganti gigi!")

    def info_mobil(self):
        print("\n--- Informasi Mobil ---")
        print(f"Merk             : {self.merk}")
        print(f"Model            : {self.model}")
        print(f"Tahun Produksi   : {self.tahun_produksi}")
        print(f"Warna            : {self.warna}")
        print(f"Nomor Polisi     : {self.nomor_polisi}")
        print(f"Kecepatan Maks   : {self.kecepatan_maksimum} km/jam")
        print(f"Bahan Bakar      : {self.bahan_bakar}")
        print(f"Kapasitas        : {self.jumlah_penumpang} penumpang")
        print(f"Status Mesin     : {'Menyala' if self.status_mesin else 'Mati'}")
        print(f"Kecepatan Sekarang: {self.kecepatan_sekarang} km/jam")
        print(f"Posisi Gigi      : {self.posisi_gigi}")
        print("-----------------------\n")

    def klakson(self):
        print(f"Mobil {self.merk} {self.model} berbunyi: Beep! Beep! 📣")

# --- Pembuatan Objek (Minimal 2) ---

# Objek 1: Mobil Keluarga
mobil_keluarga = Mobil(
    merk="Toyota",
    model="Avanza",
    tahun_produksi=2023,
    warna="Silver",
    nomor_polisi="B 1234 XYZ",
    kecepatan_maksimum=180,
    bahan_bakar="Bensin",
    jumlah_penumpang=7
)

# Objek 2: Mobil Sport
mobil_sport = Mobil(
    merk="Ferrari",
    model="488 GTB",
    tahun_produksi=2022,
    warna="Merah",
    nomor_polisi="F 888 RR",
    kecepatan_maksimum=330,
    bahan_bakar="Bensin",
    jumlah_penumpang=2
)

# --- Pemanggilan Method pada Objek ---

# Interaksi dengan mobil_keluarga
mobil_keluarga.info_mobil()
mobil_keluarga.start_engine()
mobil_keluarga.ganti_gigi(1)
mobil_keluarga.percepat(30)
mobil_keluarga.percepat(40)
mobil_keluarga.klakson()
mobil_keluarga.perlambat(20)
mobil_keluarga.info_mobil()
mobil_keluarga.stop_engine()

print("\n========================================\n")

# Interaksi dengan mobil_sport
mobil_sport.info_mobil()
mobil_sport.start_engine()
mobil_sport.ganti_gigi(2)
mobil_sport.percepat(100)
mobil_sport.percepat(150) # Akan mencapai kecepatan maksimum
mobil_sport.klakson()
mobil_sport.info_mobil()
mobil_sport.stop_engine()