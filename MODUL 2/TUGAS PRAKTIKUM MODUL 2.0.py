class Hero:
    # Private class variable untuk menghitung jumlah hero yang dibuat
    __jumlah = 0

    def __init__(self, nama, health, attPower, armor):
        # Semua atribut bersifat private
        self.__name = nama
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor

        # Atribut level dan exp
        self.__level = 1
        self.__exp = 0

        # Atribut dinamis bergantung pada level
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        self.__health = self.__healthMax

        # Tambahkan ke total jumlah hero
        Hero.__jumlah += 1

    # Property getter dan setter untuk EXP
    @property
    def gainEXP(self):
        pass  # getter wajib ada agar setter bisa berfungsi

    @gainEXP.setter
    def gainEXP(self, addEXP):
        self.__exp += addEXP

        # Cek apakah level naik
        while self.__exp >= 100:
            self.__exp -= 100
            self.__level += 1
            print(f"{self.__name} level up")

            # Rehitung atribut dinamis setelah naik level
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
            self.__health = self.__healthMax

    # Method attack
    def attack(self, musuh):
        # Setiap menyerang, hero mendapat 50 EXP
        self.gainEXP = 50

    # Property hanya getter untuk info (read-only)
    @property
    def info(self):
        return f"{self.__name} level {self.__level}:\n" \
               f"\thealth = {self.__health}/{self.__healthMax}\n" \
               f"\tattack = {self.__attPower}\n" \
               f"\tarmor = {self.__armor}"

slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)

print(slardar.info)
print()  # spasi biar rapi

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print()
print(slardar.info)
