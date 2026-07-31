class Kitob:
    def __init__(self, nomi, muallif, sahifa):
        self.nomi = nomi
        self.muallif = muallif
        self.sahifa = sahifa

    def __str__(self):
        return f"{self.nomi} ({self.muallif}) - {self.sahifa} sahifa"

    def add_auto(self, *qiymatlar):
        for i in qiymatlar:
            sorted(self.kitoblar.append(i))

    def __len__(self):
        return self.sahifa

    def __eq__(self, value):
        return self.sahifa == value.sahifa

    def __lt__(self, other):
        return self.sahifa < other.sahifa

    def __gt__(self, other):
        return self.sahifa > other.sahifa


kitob1 = Kitob("Hamsa", "Alisher Navoiy", 850)
kitob2 = Kitob("SOS", "Jon Miller", 270)
kitob3 = Kitob("Martin Iden", "Jek London", 950)
kitoblar = [kitob1, kitob2, kitob3]

for i, kitob in enumerate(kitoblar, start=1):
    print(f"{i} - {kitob}")

print(f"\n1 va 2- kitob sahifalar tengmi? ({kitob1 == kitob2})")
print(f"2 dan 3- kitob sahifalari kattami ? ({kitob2 < kitob3})")
print(f"1-dan 3-kitob kattami ? ({kitob1 > kitob3})\n")
