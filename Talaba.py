class Talaba:
    def __init__(self, ism, baho):
        self.ism = ism
        self.baho = baho

    def __str__(self):

        ortacha = sum(self.baho.values()) / len(self)

        return f"{self.ism} - {len(self)} - ta fan,o'rtacha baho: {ortacha:.1f}"

    def __len__(self):
        return len(self.baho)

    def __setattr__(self, name, value):
        if name == "baho":
            for i, baho in value.items():
                if not (0 <= baho <= 100):
                    raise ValueError("Baho 0 dan 100 oralig'ida bo'lsin")

        super().__setattr__(name, value)

    def __getattr__(self, name):
        return f"Bu atribut mavjud emas: {name}"


talaba = Talaba("Ali", {"Matematika": 95, "Fizika": 90, "Informatika": 90})
print(talaba)

print(f"Fanlar soni: {len(talaba)}")

print(talaba.yosh)