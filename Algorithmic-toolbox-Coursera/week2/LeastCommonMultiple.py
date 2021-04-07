import sys


def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x,y):
    lcm = (x*y)//gcd(x,y)
    return (lcm)


if __name__ == '__main__':
    input = sys.stdin.read()
    input_x, input_y = map(int, input.split())
    print(lcm(input_x,input_y))
