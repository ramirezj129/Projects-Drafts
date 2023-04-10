class Vault:
    def __init__(self, gallions=0, sickel=0, knuts=0):
        self.gallions = gallions
        self.sickels = sickel
        self.knuts = knuts

    def __str__(self):
        return f"{self.gallions} Galliions, {self.sickels} Sickels, {self.knuts} Knuts"

    def __add__(self, other):
        gallions = self.gallions + other.gallions
        sickels = self.sickels + other.sickels
        knuts = self.knuts + other.knuts
        return Vault(gallions, sickels, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)
