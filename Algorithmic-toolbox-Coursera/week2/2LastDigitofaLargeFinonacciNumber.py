import sys


def FibanacciNumber(n):
    if n == 0: return 0
    ans = [0,1]
    i =0

    while i < n:
        ans.append(ans[len(ans)-1] + ans[len(ans)-2])
        i+=1
    answer =  ans[len(ans)-2]
    laststr = str(answer)[-1]
    print(int(laststr))
if __name__ == '__main__':
    input = input()
    n = int(input)
    FibanacciNumber(n)
