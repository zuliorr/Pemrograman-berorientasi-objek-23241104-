class Hero:

    # === Private Class Variable ===
    __jumlah = 0   # menghitung total Hero yang dibuat

    # === Constructor ===
    def __init__(self, nama, health, attPower, armor):
        # Atribut private (base stats)
        self.__name = nama
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor

        # Atribut level & exp
        self.__level = 1
        self.__exp = 0

        # Atribut dinamis (bergantung pada level)
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        self.__health = self.__healthMax  # darah saat ini

        # Menambah jumlah Hero
        Hero.__jumlah += 1

    # === Getter untuk info (read-only property) ===
    @property
    def info(self):
        return f"""{self.__name} level {self.__level}: 
\thealth = {self.__health}/{self.__healthMax} 
\tattack = {self.__attPower} 
\tarmor = {self.__armor}"""

    # === Getter & Setter untuk EXP ===
    @property
    def gainEXP(self):
        # getter hanya agar setter bisa berfungsi (tidak digunakan)
        pass

    @gainEXP.setter
    def gainEXP(self, addEXP):
        # menambah exp
        self.__exp += addEXP
        print(f"{self.__name} mendapatkan {addEXP} exp")

        # cek level up
        while self.__exp >= 100:
            print(f"{self.__name} level up")
            self.__level += 1
            self.__exp -= 100

            # update atribut dinamis
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
            self.__health = self.__healthMax

    # === Method serangan ===
    def attack(self, musuh):
        print(f"{self.__name} menyerang {musuh.__name}!")
        # setiap serangan memberi 50 exp
        self.gainEXP = 50


# === Test Case ===
slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)

print(slardar.info)
print()

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print()
print(slardar.info)
