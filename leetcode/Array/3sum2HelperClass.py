from _bisect import bisect_right
from bisect import bisect_left

"""
source of solution **
:::https://leetcode.com/problems/3sum/discuss/7482/Fastest-Python-solution-180-ms

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.



"""

class Solution:
    def __init__(self, n):
        self.n = n

    def threeSum(self):
        f={}
        for i in self.n:f[i]=f.get(i,0)+1
        self.n=sorted(f)
        a=[]
        for i,I in enumerate(self.n):
            if not I:
                if f[I]>2:a.append((0,0,0))
            elif f[I]>1 and -2*I in f:a.append((I,I,-2*I))
            if I<0:
                t=-I
                l=bisect_left(self.n,t-n[-1],i+1)
                r=bisect_right(self.n,t//2,l)
                for J in n[l:r]:
                    K=t-J
                    if K in f and K!=J:a.append((I,J,K))
        return a


n =[1,2,0]

answer = Solution(n)

print(answer.threeSum())