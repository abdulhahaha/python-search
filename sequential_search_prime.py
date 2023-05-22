def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sequential_search_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

my_list = [7, 10, 13, 6, 17, 22, 19]

primes = sequential_search_primes(my_list)
print("Bilangan prima dalam daftar :", my_list, "adalah:")
print(primes)