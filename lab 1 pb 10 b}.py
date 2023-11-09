def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def goldbach(num):
    for f1 in range(1, num-1, 1):
        if isprime(f1):
            f2 = num - f1
            if isprime(f2):
                return f1, f2


num=int(input("Introduceti numar:"))
print(goldbach(num))