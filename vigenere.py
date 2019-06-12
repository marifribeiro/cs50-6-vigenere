from cs50 import get_string
from sys import argv, exit

# checks if argument is valid
if len(argv) != 2:
    exit("Usage: python vigenere.py keyword")
elif not argv[1].isalpha():
    exit("Usage: python vigenere.py keyword")

# give a name to argv[1]
keyWord = argv[1]
# create an array for keyword values
keyNum = []

# convert the keyword to an array of keys numbers
for i in keyWord:
    if i.isalpha() and i.isupper():
        keyNum.append(ord(i) - ord('A'))
    elif i.isalpha() and i.islower():
        keyNum.append(ord(i) - ord('a'))
    else:
        keyNum.append(ord(i))

# gets plaintext
plaintext = get_string("Plaintext: ")
# counter to loop over the key word
keyCounter = 0
#print ciphertext
print("ciphertext: ", end="")

for i in plaintext:

    # result of ciphertext
    ciphertext = ord(i) + keyNum[keyCounter]

    # if char is uppercased, keep uppercased
    if i.isupper() and ciphertext > 90:
        ciphertext = ciphertext - 26
    # if char is lowercased, keep lowercased
    elif i.islower() and ciphertext > 122:
        ciphertext = ciphertext - 26
    # if char is not alpha, keep as it is and decrease counter so it doesn't go until next char
    elif not i.isalpha():
        ciphertext = ord(i)
        if keyCounter > 0:
            keyCounter -= 1
        else:
            keyCounter = 0

    #  when the counter equals the last index of the keyNum array, reset
    if keyCounter == (len(keyNum) - 1):
        keyCounter = 0
    # if counter doesn't reach the max length of the array, increase by 1
    else:
        keyCounter += 1

    # print ciphertext
    print(chr(ciphertext), end="")

print("")