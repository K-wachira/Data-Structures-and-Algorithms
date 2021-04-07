import sys


def FibanacciNumber(n):
    if n <= 1:
        return n

    previous,   current  = 0 , 1
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(FibanacciNumber(n))
