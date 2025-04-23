class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        return self.date == other.date

d1 = Date(12, 6, 2025)
d2 = Date(12, 6, 2025)
print("Dates are equal:", d1 == d2)