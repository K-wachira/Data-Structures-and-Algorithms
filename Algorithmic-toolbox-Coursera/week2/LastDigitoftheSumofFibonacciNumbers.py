import sys
def FibanacciNumber(from_, to):
    ans = [0,1]
    i =1

    while i < to:
        ans.append(ans[len(ans)-1] + ans[len(ans)-2])
        i+=1
    digit = str(sum(ans[from_:to]))
    answer = int(digit[-1])
    return (answer)
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(FibanacciNumber(from_, to))
