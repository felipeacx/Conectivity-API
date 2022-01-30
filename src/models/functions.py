def isPrime(num):
    contador = 0
    for n in range(2, num):
        if num % n == 0:
            contador += 1
    if contador > 0:
        return False
    else:
        return True


def get_primes(num):
    result = "Los números primos de 1 a "+str(num)+" son: "
    for element in range(1, num):
        if isPrime(element):
            result += str(element)+" "
    return result
