class KilogramToPoundConverter:
    @staticmethod
    def convert(kg):
        return round(kg * 2.205, 3)

print(KilogramToPoundConverter.convert(12))
print(KilogramToPoundConverter.convert(41))