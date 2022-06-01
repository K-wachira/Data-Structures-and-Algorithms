from _bisect import bisect_right
from bisect import bisect_left

"""
source of solution **
:::https://leetcode.com/problems/3sum/discuss/7482/Fastest-Python-solution-180-ms

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.



"""

def threeSum(n):
    f={}
    for i in n:f[i]=f.get(i,0)+1
    print(f)
    n=sorted(f)
    a=[]
    for i,I in enumerate(n):
        if not I:
            if f[I]>2:a.append((0,0,0))
        elif f[I]>1 and -2*I in f:a.append((I,I,-2*I))
        if I<0:
            t=-I
            l=bisect_left(n,t-n[-1],i+1)
            r=bisect_right(n,t//2,l)
            for J in n[l:r]:
                K=t-J
                if K in f and K!=J:a.append((I,J,K))
    return a
n = [-1, 0, 1, 2, -1, -4]
threeSum(n)