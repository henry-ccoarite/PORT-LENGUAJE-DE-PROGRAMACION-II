class ConversorTemperatura:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    @classmethod
    def desde_celsius(cls, c):
        f = (c * 9/5) + 32
        return cls(f)

    @staticmethod
    def celsius_a_fahrenheit(c):
        return (c * 9/5) + 32

t1 = ConversorTemperatura.desde_celsius(25)
print(t1.fahrenheit)

print(ConversorTemperatura.celsius_a_fahrenheit(30))
