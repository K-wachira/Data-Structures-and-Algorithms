

"""
Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.

"""


"""
My approach : find every combination possible
do a loop starting with the biggest and check if its in the combination will us 0(K) best case

"""

import  itertools
S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}


def find_longest_word_in_string(S, D):

    slist = []
    allcombinations =[]
    listofwords =[]
    listofDwords = []
    inboth =[]
    longest = ""
    leng =0
    """This loop is dividing the letters and listing them independently"""
    for i in S:
        slist.append(i)

    """This loop creates nested list of all possible letter combination in a sequential manner"""
    for i in range(0, len(slist)+1):
        for subset in itertools.combinations(slist,i):
            allcombinations.append(list(subset))
    """This loop flattens the 2D array and joins the letters to form words such that you have a list of all possible words"""
    for i in allcombinations:
        listofwords.append("".join(i))
    """This just converts D into an actual list"""
    for i in D:
        listofDwords.append(i)

    """check if the word is in both lists """
    for i in listofwords:
        if i in listofDwords:
            inboth.append(i)
    """check the longest word and assign it to longest"""
    for i in inboth:
       if len(i) >leng:
        leng = len(i)
        longest = i
    """Print out the word or return it"""
    print(longest)
    return(longest)

find_longest_word_in_string(S, D)
