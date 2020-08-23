import sys


def gcd(x, y):
   while(y):
       x, y = y, x % y
   return (x)




if __name__ == '__main__':
    input = sys.stdin.read()
    input_x, input_y = map(int, input.split())
    print(gcd(input_x,input_y))
