# Import Libraries
import string
import random

# String Varabiles
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

character_number = input("How many Characters For the Password : ")

while True:
    try:
        character_number = int(character_number)
        if character_number < 6:
            print("You need at least 6 numbers")
            character_number = input("Please Enter the number again : ")
        else:
            break
    except:
        print("Pleas Enter Numbers Only !")
        character_number = input("How many Characters For the Password : ")

#print(s1)
random.shuffle(s1)
#print(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

#Separte numbeer of Characters To ===>> 30% For lowercase
#                                 ===>> 30% For uppercase
#                                 ===>> 20% For digits
#                                 ===>> 20% For punctuation


# Creating The Password
password = []

part_1 = round(character_number * (30/100))
part_2 = round(character_number * (20/100))

for i in range(part_1):
    password.append(s1[i])
    password.append(s2[i])

for j in range(part_1):
    password.append(s3[j])
    password.append(s4[j])


# Final Password
password_final = "".join(password)


# Deubugging For Final Result

# print(password)
# print("".join(password))
# print(f"Your Password Is : {password}")


# Printing Final Password
print(f"Your Password Is : {password_final}")