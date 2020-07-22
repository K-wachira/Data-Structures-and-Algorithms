def FibanacciNumber(n):
    if n == 0: return  0
    ans = [0,1]
    i =0

    while i < n:
        ans.append(ans[len(ans)-1] + ans[len(ans)-2])
        i+=1
    return ans[n]
if __name__ == '__main__':
    input_n = int(input())
    print(FibanacciNumber(input_n))
