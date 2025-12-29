class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector2D(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector2D(self.x - v.x, self.y - v.y)

    def __mul__(self, k):
        return Vector2D(self.x * k, self.y * k)

    def mostrar(self):
        return f"[{self.x}, {self.y}]"

a = Vector2D(5, 2)
b = Vector2D(1, 7)

print((a + b).mostrar())
print((a - b).mostrar())
print((a * 4).mostrar())
