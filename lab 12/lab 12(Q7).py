class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

w = Weather(["rainy", "humid", "cloudy"])
print("humid" in w)
print("sunny" in w)