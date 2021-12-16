
# this function, takes in a string p, and adds the all the numbers in the value p
# creating a new string which becomes out new p
# this process is repreted recursively untill p is of len 1, or p is less than 10 

def super_digit(p): 
    if int(p) < 10: # base case that checks if p is less than 10 
        return int(p) # return int if base case is true
    else:
        temp = 0 #this will be the new p if basecase is not true 
        for i in p: # loop p,
            temp += int(i) # add all the values in p to create a new and smaller p
        return super_digit(str(temp)) # recurse on the newly created p value.




# This function takes a number k and string n, and creates
# k instances of n and returns a concatenated string of all the instances
def concatenate(k, n):
    out = "" # return value 
    while k > 0: # loop until n is repreicated k times
        out += n # append new instance of n to the other concatenated instances 
        k -=1  # mark that instance of n as done 
    return out  # return all instance in a single string which will serve as p value 



# Main function that takes in k and n , where k is an int and n is a string 
def main(k , n):
    p = concatenate( k, n ) # create value p

    supper = super_digit(p) # calculate supper digit of p

    print(supper)
    return supper

main( 3, "148")