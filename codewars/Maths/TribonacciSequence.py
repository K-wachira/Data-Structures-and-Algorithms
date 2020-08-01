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

def tribonacci2(s,n):
    if n ==0: return []
    for i in range(2,n):
        s.append(s[i-2]+s[i-1]+s[i])
    return (s)

def tribonacci3(signature,n):
    while len(signature) <n:
        signature.append(sum(signature[-3:])) #slice the signature to the last three digits
        # and append their sum
    return (signature)


signature = [1, 1, 1]
n = 10
# print(tribonacci(signature, n))
print(tribonacci2(signature,n))
print(tribonacci3(signature,n))