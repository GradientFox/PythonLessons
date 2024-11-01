import sympy

def generate_prime(num):
    for i in range(1, num+1):
        if sympy.isprime(i):
            yield i


map = list(generate_prime(100))
print(map)