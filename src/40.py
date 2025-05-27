def find_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    elif n <= 3:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def max_subarray(nums: list[int]) -> tuple[int, int]:
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], nums[i] + current_sum)
        if current_sum > max_sum:
            max_sum = current_sum
    return (max_sum, current_sum)

def check(s: str) -> bool:
    vowels = 'aeiou'
    for char in s:
        if char.lower() not in vowels:
            return False
    return True

def main():
    print("Hello, world!")
