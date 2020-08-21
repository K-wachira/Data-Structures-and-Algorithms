"""
You are given an integer, .
Your task is to print an alphabet rangoli of size .
(Rangoli is a form of Indian folk art based on creation of patterns.)

https://www.hackerrank.com/challenges/alphabet-rangoli/problem

eg
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""



def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    n = size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        # print((s[::-1] + s[1:]).center(5 * n - 3, "-"))

        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
    print('\n'.join(L[:0:-1] + L))








    # your code goes here

size = 10
print_rangoli(size)