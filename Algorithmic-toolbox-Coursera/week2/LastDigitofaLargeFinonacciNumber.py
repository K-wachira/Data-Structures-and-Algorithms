def FibanacciNumber(n):
    ans = [0,1]
    i =0

    while i < n:
        ans.append(ans[len(ans)-1] + ans[len(ans)-2])
        i+=1
    ans = ans[:n]
    return ans[len(ans)-1]
if __name__ == '__main__':
    input_n = int(input())
    print(FibanacciNumber(input_n))
