import sys
def creategrid(r, c):
    grid = []
    for i in range(r):
        rows = []
        for i in range(c):
            rows.append("") 
        grid.append(rows)
    return grid 

def encrypt(r,text):
    c = len(text)
    grid  = creategrid(r, c)
    col = 0
    row = 0
    index = 0 
    while  col < c:
        letter = text[index]
        grid[row][col] = letter
        col +=1 
        row +=1 
        index +=1
        if row == r:
            row = 0
    return grid

def dencrypt(r,message):
    word = ""
    col = 0
    row = 0
    while  col < len(message[0]):
        word += message[row][col]
        col +=1 
        row+=1
        if row == r:
            row = 0
    return word

def printEncryptedMessage(grid):
    output = ""
    for i in grid:
        output += "".join(i)
    return output


def printGrid(grid):
    for i in grid:
        print(i, end ="\n")





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

