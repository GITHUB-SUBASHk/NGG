def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

def is_perfect_cube(n):
    return round(n ** (1/3)) ** 3 == n
