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