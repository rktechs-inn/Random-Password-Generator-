import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#chars = [letters, numbers,symbols]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)

#Haed level
#Took empty list to append the characters as per input
#pwd_list = ""
pwd_list =[]

for char in range(0, nr_letters):
    pwd_list.append(random.choice(letters))
    # pwd_list += random.choice(letters)

for char in range(0, nr_numbers):
    pwd_list.append(random.choice(numbers))
#     pwd_list += random.choice(numbers)

for char in range(0, nr_symbols):
    pwd_list.append((random.choice(symbols)))
#     pwd_list += random.choice(letters)

print(pwd_list)
random.shuffle(pwd_list)
print(pwd_list)  #This will print in format of list: ['1','g','$',....]

#To print in form of text(string) or pwd: 1h5rRK$^...
pwd = ""
for char in pwd_list:
    pwd += char

print(f"Your password is {pwd}")




