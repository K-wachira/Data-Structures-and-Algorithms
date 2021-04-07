import  math
def supernaturalNumbers(numbers):

    numbers.sort()
    print(numbers)
    foundNatural = set()
    foundIntegers = set()
    supernatural = set()

    supernaturala = set()
    supernaturalb = set()
    for i in numbers:
        if math.ceil(i) > 0:
            foundNatural.add(i)
        if math.floor(i) == i:
            foundIntegers.add(i)
        if math.floor(i) == i:
            if i%2 == 0 and i != 0:
               supernaturala.add(i)
            if i % 2 > 0:
                supernaturalb.add(i)

    supernaturalb = list(supernaturalb)
    supernaturalb.sort()
    nsnb = []
    psnb = []
    for i in supernaturalb:
        if i < 0:
            nsnb.append(i)
        else:
            psnb.append(i)
    nsnb.sort(reverse=True)
    psnb.extend(nsnb)
    supernaturala = list(supernaturala)
    supernaturala.sort()

    if 0 in numbers:
        supernaturala.append(0)
    supernaturala.extend(psnb)


    numbers.clear()
    foundIntegers = list(foundIntegers)
    foundIntegers.sort()
    numbers.append(list(foundNatural))
    numbers.append((list(foundIntegers)))
    numbers.append(list(supernaturala))

    return numbers


numbers= [2, 5, 6, 0, -9, 8, -14, 25, -5, 5]

print(supernaturalNumbers(numbers))
