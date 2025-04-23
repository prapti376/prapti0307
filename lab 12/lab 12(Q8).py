class String:
    def __init__(self, text=""):
        self.text = text

    def __iadd__(self, other):
        self.text += other
        return self

    def toLower(self):
        self.text = self.text.lower()

    def toUpper(self):
        self.text = self.text.upper()

    def display(self):
        print(self.text)

s = String("Hello")
s += " World"
s.display()
s.toLower()
s.display()
s.toUpper()
s.display()