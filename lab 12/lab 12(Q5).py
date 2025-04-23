class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes
        self.normalize()

    def normalize(self):
        self.hours += self.minutes // 60
        self.minutes %= 60

    def add_time(self, other):
        return Time(self.hours + other.hours, self.minutes + other.minutes)

    def display(self):
        print(f"{self.hours} hour(s) and {self.minutes} minute(s)")

t1 = Time(6, 50)
t2 = Time(1, 40)
t3 = t1.add_time(t2)
t3.display()