

def sumOfN(n): # function definition 
    output = 0 # results will be stored in this variable
    for i in range(1, n+1): # loop from 1 to n, I have put n+1 so as to include the nth number 
        output +=i
    return output # finally return the sum of the n numbers including the n 


print(sumOfN(1000000000))
500,000,000,500,000,000