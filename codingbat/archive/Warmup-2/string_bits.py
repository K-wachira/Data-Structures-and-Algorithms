"""
Given a string, return a new string made of every other char
starting with the first, so "Hello" yields "Hlo".

"""


def string_bits(str):
    empty = []
    count = 0
    for i in str:
        count += 1

        if count % 2 > 0:
            empty.append(i)

    return "".join(empty)