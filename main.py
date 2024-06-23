import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Fastest Password Generator and Simple login/ sign up system system!")
print("With this password generator, you can easily create a random password and kick off with your new account ")


account = input("Do you have an account? If you do and you just want to login then respond with exactly what you see in the quotes:'Yes.\n If you have and account but would love to generate a new password, then type 'new_password'.\n if you dont have any of these then just type No ")
if account == 'Yes':
  username = input("please enter your username: ")
  password = input("please enter your password: ")
  print(" Logged in successfully")
elif account == 'new_password':
  username = input("please enter your username: ")
  old_password = input("please enter your current password: ")
  nr_letters= int(input("For your new password, how many letters would you like in your password?\n"))
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))
  password_list = []
  for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password_list.append(random_char)
  for char in range(1, nr_symbols + 1):
    random_char = random.choice(numbers)
    password_list += random_char
  for char in range(1, nr_numbers + 1):
    password_list += random.choice(letters)

  print(password_list)
  random.shuffle(password_list)
  print(password_list)

  new_password = ""
  for char in password_list:
    new_password = new_password + char

  print(f"Your new password is: {new_password}")
  print("please enter your login credentials again")
  username2 = input("please enter your username: ")
  password2 = input("please enter your password: ")
  if username2 == username and password2 == new_password:
    print("Logged in successfully")
  else:
    print("Incorrect username or password")
else:
  print("Please create an account")
  username = input("please enter your username: ")
  password = input("please enter your password: ")
  print("Your account has been created succesfully!")
  print("Please enter your login credentials again")
  username2 = input("please enter your username: ")
  password2 = input("please enter your password: ")
  if username2 == username and password2 == password:
    print("Logged in successfully")
  else:
    print("Incorrect username or password")

