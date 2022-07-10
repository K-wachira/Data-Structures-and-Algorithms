
def matchingSocks(socks_array):
    #Step 1
    color_group = {}   # dictionary to store the group of colors of socks and the count of socks in that group
    pair_count = 0   # variable that will keep track of the number of pairs we have encountered

    for socks_color in  socks_array:              # loop through the socks in the input socks_array
        if socks_color in  color_group.keys():           # check if the socks color is already defined in the group of socks 
                            # if the color is already defined in the group increment the 
                            # count of socks in that group by 1
            color_group[socks_color] += 1
            
        else:                                                                         # if the color of socks is not among the color of socks already seen						#then create the new color of socks in the group of socks and give 						# it a value of one.
            color_group[socks_color] = 1
    #Step 2
   
    for  count_of_socks in color_group.values(): # loop over the color grouped socks 
                            # and get the number of socks in each group
        pair_count += count_of_socks//2       # for every number of socks in each group divide it by 2 
                                    #and floor the results, then add the results to the variable ‘pair_count’

    #Step 3

    return pair_count  # finally return the value stored in the pair_count as that will be the number of pairs of sock 



array1 = [1, 3, 11, 1, 3, 12, 1, 3, 13, 1, 3, 14, 1, 3, 15, 1, 3, 16, 1, 3, 17, 1, 3, 18, 1, 3, 19, 1, 3, 20]
array2 =[1, 3, 5, 6, 7, 8, 9, 9, 1, 3, 5, 6, 7, 8, 9, 10, 1, 3, 5, 6, 7, 8, 9, 11, 1, 3, 5, 6, 7, 8, 9, 12, 1, 3, 5, 6, 7, 8, 9, 13, 1, 3, 5, 6, 7, 8, 9, 14, 1, 3, 5, 6, 7, 8, 9, 15, 1, 3, 5, 6, 7, 8, 9, 16, 1, 3, 5, 6, 7, 8, 9, 17, 1, 3, 5, 6, 7, 8, 9, 11]


# Testing 
# Case 1 
if matchingSocks(array1) == 10:
    print("Test case 1 passed having returned {10} pairs")
else:
    print("Test case 1 Failed")
#Case 2
if matchingSocks(array2) == 36:
    print("Test case 2 passed having returned {36} pairs")
else:
    print("Test case 2 Failed")
