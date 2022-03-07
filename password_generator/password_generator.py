#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print(len(letters))
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=[]
for i in range(0,nr_letters):
  new_letter=random.choice(letters)
  password.append(new_letter)
for i in range(0,nr_numbers):
  new_number=random.choice(numbers)
  password.append(new_number)

for i in range(0,nr_symbols):
  new_symbol=random.choice(symbols)
  password.append(new_symbol)
print(password)
password_str=""
password_str=password_str.join(password)
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print(f"your easy password : {password_str}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_str=""
random.shuffle(password)
print(password)
password_str=password_str.join(password)
print(f"your hard password : {password_str}")