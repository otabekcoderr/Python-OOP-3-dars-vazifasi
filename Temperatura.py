class Temperatura:
    def __init__(self, daraja, birlik):
        self.daraja = daraja
        self.birlik = birlik

    def __str__(self):
        return f"{self.daraja} {self.birlik}"

    def __repr__(self):
        return f"Temperatura({self.daraja}, '{self.birlik}')"

    def __eq__(self, value):
        return self.daraja == value.daraja

    def __lt__(self, other):
        return self.daraja < other.daraja

    def __le__(self, other):
        return self.daraja <= other.daraja

    def __gt__(self, other):
        return self.daraja > other.daraja

    def __ge__(self, other):
        return self.daraja >= other.daraja


tem = Temperatura(36.6, "C")
tem1 = Temperatura(39.6, "C")
print(f"1 2dan kattami ? {tem >= tem1}")

print(tem)
print(tem1)
