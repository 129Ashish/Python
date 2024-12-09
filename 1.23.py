#for loop using continue and break statements :
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, n):
        if n % i == 0:
            return False  # n is divisible by i, so it's not prime
    return True  # n is prime


def get_prime_numbers(n):
    """Get all prime numbers up to n."""
    prime_numbers = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

def main():
    n = int(input("Enter a number: "))
    prime_numbers = get_prime_numbers(n)
    print("Prime numbers up to", n, "are:")
    print(prime_numbers)

main()