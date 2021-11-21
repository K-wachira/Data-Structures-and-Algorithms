

def merge_sort(array):
    n = len(array)


    if n <= 1:
        return array
    mid = n // 2
    left = array[:mid]
    right = array[mid:]
    r = merge_sort(left)
    l = merge_sort(right)
    return merge(r, l)

def merge(left, right):
    # 7. Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers when iterating through the lists.
    output = []
    i = j = 0

    # 8. Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # 9. Compare the elements at every position of both lists during each iteration
        if left[i] < right[j]:
            # output is populated with the lesser value
            output.append(left[i])
            # 10. Move pointer to the right
            i += 1
        else:
            output.append(right[j])
            j += 1
    # 11. The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output


def merges(left, right):
    out = []
    ptr1 = 0
    ptr2 = 0
    r = len(left)
    l = len(right)
    while ptr1 < r and ptr2 < l:
        if left[ptr1] < right[ptr2]:
            out.append(left[ptr1])
            ptr1 += 1
        else:
            out.append(left[ptr2])
            ptr2+=1
    if ptr1< r: out.extend(left[ptr1:])
    
    if ptr2 < l: out.extend(right[ptr2:])
    
    return out



import sys

inpt = open(sys.argv[1])

array = []
for i in inpt:
    array.append(int(i))
merge_sort(array)
