def isUnique(string: str):
    return len(string) == len(set(string))


def isUniqueII(string: str):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]: return False
    return True

testcases = {
    "kelvin": True,
    "": True,
    "wachira": False,
    "abcdefgh": True,
    "aea": False
}
for key, value in testcases.items():
    if isUniqueII(key) == value:
        print("OK: {} {}".format(isUniqueII(key), key))
    else:
        print("Case Failed {} {}".format(isUniqueII(key), key))
