def gcd(a,b):
    if b == 0:
        print(a)
    gcd(b, a%b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    (gcd(a,b))
