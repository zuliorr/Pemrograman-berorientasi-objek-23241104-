class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama            # public attribute
        self.__saldo = saldo        # private attribute

    def lihat_saldo(self):
        # Method internal untuk melihat saldo
        print(f"Saldo {self.nama}: Rp{self.__saldo}")

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil setor Rp{jumlah}")
        else:
            print("Jumlah setor harus lebih dari 0!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Berhasil tarik Rp{jumlah}")
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")


# ==== Program utama ====
akun_budi = RekeningBank("Budi", 1000000)
print(f"Nama pemilik rekening: {akun_budi.nama}")

# Mengakses saldo lewat method (benar)
akun_budi.lihat_saldo()

# Mencoba akses langsung dari luar (akan ERROR)
print(akun_budi.__saldo)   # ERROR: AttributeError
