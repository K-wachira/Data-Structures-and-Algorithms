
"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:"""



def romanToInt( s) :
    number = 0
    "MCDLXXVI"
    'IV IL '
    'XL XC '
    'CD DM'
    for i in range(len(s)-1):
        if s[i] == 'I' and s[i+1] == 'V':
            number = number+ 4
            s = s[:i] +'PP'+ s[i+2:]
        elif s[i] == 'I' and s[i+1] == 'X':
            number = number+ 9
            s = s[:i] +'PP'+ s[i+2:]
        elif s[i] == 'X' and s[i+1] == 'L':
            number = number+ 40
            s = s[:i] +'PP'+ s[i+2:]
        elif s[i] == 'X' and s[i+1] == 'C':
            number = number+ 90
            s = s[:i] +'PP'+ s[i+2:]
        elif s[i] == 'C' and s[i+1] == 'M':
            number = number+ 900
            s = s[:i] +'PP'+ s[i+2:]
        elif s[i] == 'C' and s[i+1] == 'D':
            number = number+ 400
            s = s[:i] +'PP'+ s[i+2:]



    for i in range(len(s)):

        if s[i] == 'M':
            number = number+ 1000
        elif s[i] == 'D':
            number = number+ 500

        elif s[i] == 'C':
            number = number +100

        elif s[i] == 'L':
            number = number + 50

        elif s[i] == 'X':
            number = number+ 10

        elif s[i] == 'V':
            number = number+5

        elif s[i] == 'I':
            number = number+ 1

    print(number)
    return number


s = "MCDLXXVI"
    # 'MCMXCV'
romanToInt(s)



