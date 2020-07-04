"""

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
 because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

"""
import math

def myAtoi(str):
    strippedstr = ''
    isNegative = False
    pos_num = ''
    started = False

    for i in range(len(str)):
        if str[i] != " ":
            started = True
            strippedstr = strippedstr + str[i]
        elif started:
            if str[i] == ' ':
                break

    endofStrippedstr = len(strippedstr)
    for i in range(len(strippedstr)):
        if strippedstr[i] == '.':
            endofStrippedstr = i

    if strippedstr[0] == '-':
        print('isnegative')
        isNegative = True
        strippedstr = strippedstr[1:endofStrippedstr]
    elif strippedstr[0] == '+':
        strippedstr = strippedstr[1:endofStrippedstr]


    elif strippedstr[0] != '-':
        strippedstr = strippedstr[0:endofStrippedstr]
    print(strippedstr)
    for n in range(len(strippedstr)):
        print(is_integer(strippedstr[n]))

        if is_integer(strippedstr[n]):
            pos_num = pos_num + strippedstr[n]
        elif not is_integer(strippedstr[n]):
            print("falsemode")
            if len(pos_num) > 0:
                pos_num = pos_num
                break
            else:
                return 0

    try:
        if isNegative:
            pos_num = int(pos_num) * -1
        else:
            pos_num = int(pos_num) * 1
    except ValueError:
        return 0

    """check if number is withn range of 32 bit"""

    if (pos_num) in range(int(math.pow(-2, 31)),
                          int(math.pow(2, 31) - 1)):
        return pos_num
    elif pos_num < int(math.pow(-2, 31)):
        return (int(math.pow(-2, 31)))
    else:
        return (int(math.pow(2, 31)) - 1)


def is_integer(n):
    try:
        float(int(n))
    except ValueError:
        return False
    else:
        return float(n).is_integer()


str = "-2147483649"
myAtoi(str) 