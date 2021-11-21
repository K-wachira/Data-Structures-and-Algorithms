#bubble sort algorithm 
import sys 

def bubble_sort(array):

    for index in range(1, len(array)):
        temp = index 
        while temp and array[temp-1] > array[temp]:
            array[temp-1], array[temp] = array[temp], array[temp-1]
            temp = temp-1
    print(array)




inpt = open(sys.argv[1]) 
inputarray = []
for line in inpt:
    inputarray.append(int(line))
    #print(line)

print(inputarray)
bubble_sort(inputarray)
