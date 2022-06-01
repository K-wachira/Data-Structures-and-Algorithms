"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
"""
def isAlienSorted(words, order):
    f = {' ': 0}
    for i, l in enumerate(order):
        f[l] = f.get(l, i) + 1
    for i, w in enumerate(words):
        for x, j in enumerate(words[i]):
            if i <= len(words) - 2:
                if len(w) > len(words[i + 1]):
                    words[i + 1] = words[i + 1] + "   x" #did this so as to ensure every letter can be compared to something
                if f[j] > f[words[i + 1][x]]:
                    return False
                elif f[j] < f[words[i + 1][x]]:
                    break
    return True
    # create a dictionary from the order
    # for i,w in enumerate(words)
    #   check if word[i-1] > word[w] : return False
    # return True
words =["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
order = "zkgwaverfimqxbnctdplsjyohu"
print(isAlienSorted(    words, order))