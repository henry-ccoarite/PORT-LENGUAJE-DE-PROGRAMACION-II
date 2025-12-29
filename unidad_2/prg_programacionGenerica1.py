from typing import TypeVar

T = TypeVar('T', int, float)

def sumar(a: T, b: T) -> T:
    return a + b

print(sumar(5, 10))
print(sumar(3.5, 2.5))
