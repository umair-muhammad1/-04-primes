from math import sqrt



def isprime(p):
    if p <= 1:
        return False
    for d in range(2, int(sqrt(p)) + 1):
        if p % d == 0:
            return False
    return True

#### Fonction principale


def main():

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
