import time
import sys

def sumOfN(n): # function definition 
    output = 0 # results will be stored in this variable
    for i in range(1, n+1): # loop from 1 to n, I have put n+1 so as to include the nth number 
        output +=i
    return output # finally return the sum of the n numbers including the n 


inpt = open(sys.argv[1]) 
for line in inpt:
    print("Running test case where n is {}".format(line), end="")
    start_time = time.time()
    result = sumOfN(int(line))
    print("and the sum of all digits in its range is", result)
    print("It took %s seconds to run" % (time.time() - start_time))
    print("__________________________________ \n\n")


