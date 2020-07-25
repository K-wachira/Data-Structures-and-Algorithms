"""
As a person of an old generation, you are lost in the ocean of abbreviations that young people use on the internet nowadays, like LMAO, AFAIK, BRB, BAE, etc. You want to converse with your grandchildren with their language though. So you decided to write a program that quickly checks the meaning of any abbreviation they will throw you. One of your grandson gave you the list of all known abbreviations in abbrList, and a list of expressions that may match one or none of these abbreviations.
"""

def afaik(abbrList, expressions):
    newExpressions = []
    small = ''
    returnlist = []

    for i,l in enumerate(expressions):
        ",".join(l)
        for j in l:
            if j.isupper():
                small = small+j


        newExpressions.append(small)
        small = ''

    for i in abbrList:
        if i in newExpressions:
            returnlist.append(newExpressions.index(i))
        else:
            returnlist.append(-1)
    return returnlist





    pass
abbrList = ["LMAO", "AFAIK", "LOL", "TLDR"]
expressions = ["As Far As I Know", "Rolling Laughing Out Loud", "Laughing Out Loud", "Be Right Back", "Before Anything Else"]

print(afaik(abbrList,expressions))