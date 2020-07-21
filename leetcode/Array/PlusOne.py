def plusOne(digits):
    number = ""
    for i in digits:
        number = number+ str(i)
    intNumber = int(number)+1
    digits.clear()
    for i in str(intNumber):
        digits.append(int(i))
    return (digits)

digits = [9,9]

(plusOne(digits))