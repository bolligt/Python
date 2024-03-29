#Password Generator Project
##### This code is supplied by the instructor#####
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

##### Everything below here is my code for the solution #####
password = ""

for letter in range(nr_letters):
  #password += random.choice(letters) is an alternative way of doing this
  password += letters[random.randint(0,len(letters)-1)]

for symbol in range(nr_symbols):
  password += symbols[random.randint(0,len(symbols)-1)]

for number in range(nr_numbers):
  password += numbers[random.randint(0,len(numbers)-1)]

print(f"Easier password: {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ""

for letter in range(nr_letters):
  password += letters[random.randint(0,len(letters)-1)]

for symbol in range(nr_symbols):
  password += symbols[random.randint(0,len(symbols)-1)]

for number in range(nr_numbers):
  password += numbers[random.randint(0,len(numbers)-1)]

# Convert string to list
password = list(password)
# Shuffle the order of the items in the list
random.shuffle(password)
# Turn the shuffled list back into a string
password = ''.join(password)

print(f"Harder password: {password}")