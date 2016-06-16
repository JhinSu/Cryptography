import sys
import os
from string import ascii_lowercase


#Get File Input and Cipher
def filePath():
    #Ask User for File Path
    user_input = input("File Path: ")

    #Example: C:\Users\John\Desktop\Caesar Script.txt
    assert os.path.exists(user_input), "File Path Invalid: " + str(user_input)
    file = open(user_input, 'r+')

    #Get First Line
    encryptedCipher = file.readline()
    encryptedCipher = encryptedCipher.lower()
    return encryptedCipher

#Frequency Analysis
def freqAnalysis(l, encryptedCipher):
    count = 0

    for i in encryptedCipher:
        if (i == l):
            count += 1

    return '%.3f' % round(count/len(encryptedCipher), 3)

#Get cipher from file
cipher = filePath()
print(cipher)

#Find the frequency that each letter occurs at
for letter in ascii_lowercase:
    print(letter, freqAnalysis(letter, cipher))
