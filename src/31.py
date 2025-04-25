def find_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def lcm(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)

def gcd(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x
