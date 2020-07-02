"""Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000."""


"""
    Approach:
    
    have a string be a pivot - center of the palindrom 
    check if left side and right side are equal if so continue until other wise and break
    returning the so far palindrome
    
    *
    even Palindrome abba which has two pivots at the center 
    odd Palindrome aba which has one pivot at the center
    *
    
    second function gets the palindromes -ExpandAndCheckPalindromeAtThisIndex-
    and assigns it to a variable in the for loop on the first function 
    
    the maxPal is updated with the longest palindrome so far
    
    NB when you want to get the longest string between strings you can use
        max( stringa, stringb , stringc , key=len)
        
        the key is used to specify what should be considered when choosing max and 
        in this case its the length (len)


"""



def longestPalindrome(s):

        maxPal =''

        for i in range(len(s)):
            forodd = ExpandAndCheckPalindromeAtThisIndex(s, i - 1, i)
            foreven = ExpandAndCheckPalindromeAtThisIndex(s, i - 1, i + 1)
            maxPal =max(maxPal, (forodd),foreven, key=len)
        print(maxPal)
        return maxPal


def ExpandAndCheckPalindromeAtThisIndex( s, i, j):
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i -= 1
            j += 1
        return s[i + 1:j]

s = 'a'
longestPalindrome(s)
