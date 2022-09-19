

import string
import random

list1 = list(string.ascii_lowercase)
list2 = list(string.ascii_uppercase)
list3 = list(string.digits)
list4 = list(string.punctuation)

characters_number = input("how maney character for the password?: ")

while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6 :
            print("you need at least 6 characters")
            characters_number = input("pleas enter the number again:")
        else:
                break
    except:
        print("please enter numbers only")
        characters_number = input("how maney character for the password?: ")

random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)
random.shuffle(list4)

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))


passowrd = []

for i in range(part1):
    passowrd.append(list1[i])
    passowrd.append(list2[i])

for i in range(part2):
    passowrd.append(list3[i])
    passowrd.append(list4[i])

random.shuffle(passowrd)    

passowrd = "".join(passowrd[0:])
print(passowrd)