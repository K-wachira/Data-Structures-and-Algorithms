from sys import stdin


def FibanacciNumber(n):
    if n == 0: return 0
    ans = [0,1]
    i =1
    listofSquares =[]
    while i < n:
        ans.append(ans[len(ans)-1] + ans[len(ans)-2])
        i+=1

    for i in ans:
        listofSquares.append(i*i)

    digit = str(sum(listofSquares))
    return (int(digit[-1]))
if __name__ == '__main__':
    input_n =int(input())
    print(FibanacciNumber(input_n))