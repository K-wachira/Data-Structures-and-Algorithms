    
def creategrid(r, c):
    grid = []
    for i in range(r):
        rows = []
        for i in range(c):
            rows.append("") 
        grid.append(rows)
    return grid 

def gencrypt(r,text):
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


def gdencrypt(r,text):
    c = len(text)
    grid  = creategrid(r, c)
    col = 0
    row = 0
    index = 0 
    while  col < c:
        letter = text[index]
        letter = grid[row][col]

        col +=1 
        row +=1 
        index +=1
        if row == r:
            row = 0
    return grid



def printEncryptedMessage(grid):
    output = ""
    for i in grid:
        output += "".join(i)
    return output


def printGrid(grid):
    for i in grid:
        print(i, end ="\n")





import math

def encryptText(key, text):
    end = len(text)
    rotation = 0 
    pos = 0
    index = 0
    encrypted_message  = ""
    while index < end:
        encrypted_message += text[pos]
        pos = pos + key
        index += 1
        if pos >= end:
            rotation +=1
            pos = rotation
    return encrypted_message




def dencryptText(key, text):
    slow= 0 
    fast = math.floor(len(text)/key)
    out = ""
    while fast < len(text):
        out += text[slow]
        out +=  text[fast]
        slow+=1 
        fast+= 1
    return out

encrypted_message = encryptText(4, "Plain text" )
print(encrypted_message)
xx = gencrypt( 4, "Plain text")
print(printEncryptedMessage(xx))

# dencrypted_message= dencryptText(3,encrypted_message )
# print( dencrypted_message)
