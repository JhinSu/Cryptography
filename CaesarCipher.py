import sys
import os

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

#Brute Force
def bruteForce(n, encryptedCipher):
    result = ''

    for letter in encryptedCipher:
        if letter.isalpha():
            num = ord(letter)
            num += n

            if num >ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26

            result += chr(num)
        else:
            result += letter     
    
    return result


cipher = filePath()
print("Cipher: " + cipher)

#Print Out Each Possible Outcome
for shift in range(1, 27):
    print(shift, bruteForce(shift, cipher))
