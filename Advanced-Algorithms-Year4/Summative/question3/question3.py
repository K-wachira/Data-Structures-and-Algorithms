import sys

# This function takes in two int, and uses the intergers to create a new empty grid.
def creategrid(r, c):
    grid = [] #initla empty grid
    for i in range(r): # loop to create r number of rows
        rows = [] # each row should have a unique new array to avoid memory dublication
        for i in range(c): # create c number of colums 
            rows.append("")  
        grid.append(rows)
    return grid  # return a full grid with empty strings as its items

# the encrytion algorithm 
def encrypt(r,text): # take in a key as input and a message that is supposed to be decrypted
    c = len(text) # 
    grid  = creategrid(r, c) # create a grid that fits the given input criteria
    col = 0
    row = 0
    index = 0  # keepts track of the characters to be encrypted next 
    while  col < c:  # loop through the whole message to be encrypted
        letter = text[index] # take one character at a time 
        grid[row][col] = letter # append the character on the grid 
        # go to next column and next row diagonally 
        col +=1  
        row +=1 
        index +=1 # jump to the next character
        if row == r: # keeps track of whether we have reached the bottom of the grid
            row = 0 # jumps back up if so 
    return grid


# This function takes in a key and encrpted message and return the approriate decrypted message
def dencrypt(r,message):
    word = "" # this will be where we store the decrypted message
    col = 0 
    row = 0
    while  col < len(message[0]): # loop through the whole encrpted message
        word += message[row][col] # takes the correct character from the grid and puts it in the var word
        # go to next column and next row diagonally 
        col +=1  
        row+=1
        if row == r: # keeps track of whether we have reached the bottom of the grid
            row = 0 # jumps back up if true
    return word # return the decrypted word

def printEncryptedMessage(grid): # prnts a pretty version of the encrypted message
    output = ""
    for i in grid:
        output += "".join(i)
    return output


def printGrid(grid): # prints out the encryption grid
    for i in grid:
        print(i, end ="\n")




# This is taking in the inputs this script should be run on terminal and the should get a text file as an arguiment 

inpt = open(sys.argv[1]) 
for line in inpt:
    line = line.split()
    key = int(line[0])
    text = str(" ".join(line[1:]))
    print("Running test case where Key is {} and message is {}".format(key, text), end="\n")
    message_encrypted = encrypt( key, text)
    print("Encrypted message is : ", printEncryptedMessage(message_encrypted))
    message_decrypted = dencrypt( key, message_encrypted)
    print("Decrypted message is : ", message_decrypted)

    print("*"*15, "\n\n")



print("#"*20)
import time
print("Running test case where key is {}".format(3))
start_timea = time.time()
result = encrypt(3, "Plain Text")
message_decrypted = dencrypt( 3, result)

print("It took %s seconds to run" % (time.time() - start_timea))
timea = time.time() - start_timea
print("__________________________________ \n\n")


print("#"*20)

print("Running test case where key is {}".format(2))
start_time2 = time.time()
result = encrypt(2, "Plain Text")
message_decrypted = dencrypt( 2, result)

print("It took %s seconds to run" % (time.time() - start_time2))
time2 = time.time() - start_timea
print("__________________________________ \n\n")


if timea > time2:
    diff =  timea - time2
    print("Key {} takes {} more to run compared to key {}.".format( 3,diff, 2 ))

if timea < time2:

    diff =  time2 - timea

    print("Key {} takes {} more to run compared to key {}.".format( 2,diff, 3 ))