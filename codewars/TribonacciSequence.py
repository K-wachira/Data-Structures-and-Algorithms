"""
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
"""

def tribonacci(signature, n):
    if n == 0: return []
    for i in range(n):
        signature.append(signature[i+2]+signature[i+1]+ signature[i])
    return signature[:n]


signature = [1, 1, 1]
n = 10
print(tribonacci(signature, n))