def is_prime(n):
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_factors(n):
    factors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            factors.append(i)
    return sorted(factors)

# Example usage:
num = 36
print("Factors of", num, ":", get_factors(num))
