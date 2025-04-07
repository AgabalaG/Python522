class WeightConverter:
    def __init__(self, kilograms):
        if not isinstance(kilograms, (int, float)):
            raise ValueError("Килограммы должны быть заданы только числами.")
        self.kilograms = kilograms

    def to_pounds(self):
        pounds = self.kilograms * 2.20462
        return round(pounds, 3)

weight1 = WeightConverter(12)
print(f"{weight1.kilograms} кг => {weight1.to_pounds()} фунтов")

weight2 = WeightConverter(41)
print(f"{weight2.kilograms} кг => {weight2.to_pounds()} фунтов")
