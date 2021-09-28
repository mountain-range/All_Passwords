#This program provides all possibilities of an 8 digit password

import random

char = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ":", ";", "'", "<", ",", ">", ".", "?", "/", "[", "]", "{", "}", "|", "-", "=", "+", "_", "~", "`", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "a", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
codes = []
x = 0
while True:
    temp = random.choice(char)+random.choice(char)+random.choice(char)+random.choice(char)+random.choice(char)+random.choice(char)+random.choice(char)+random.choice(char)
    try:
        codes.index(temp)
    except ValueError:
        codes += [temp]
        print(temp)
    x += 1
    # The x was for other calculations
