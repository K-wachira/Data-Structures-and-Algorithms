def reverseInParentheses(inputString):
    pass
    reversed = ""
    start = False
    for i, n in enumerate(inputString):
        if n == '(':
            start = True
        elif n == ')':
            start = False


        if start:
            reversed = reversed+ inputString[i+1]
        elif not  start:
            pass
        else:
            reversed = reversed + n

    print(reversed)

inputString = "(bar)s"
reverseInParentheses(inputString)