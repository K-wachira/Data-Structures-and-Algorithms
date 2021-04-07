from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous , current, sums= 0 ,1,1

 
    for _ in range(n - 1):
        previous, current = current, previous + current
        sums += current * current

    return sums % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
    
    
    
# from sys import stdin
# def FibanacciNumber(n):
#     if n == 0: return 0
#     ans = [0,1]
#     i =1
#     listofSquares =[]
#     while i < n:
#         ans.append(ans[len(ans)-1] + ans[len(ans)-2])
#         i+=1

#     for i in ans:
#         listofSquares.append(i*i)

#     digit = str(sum(listofSquares))
#     return (int(digit[-1]))
# if __name__ == '__main__':
#     input_n =int(input())
#     print(FibanacciNumber(input_n))