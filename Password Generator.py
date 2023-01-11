"""Password Generator"""

import string
import random


print("Welcome To The Password Generator!")

the_length: int = int(input("Enter The Desired Lenght Of Your Password: ")) 

letters = string.ascii_letters
the_numbers = string.digits
the_symbols = string.punctuation

all_letters = letters + the_numbers + the_symbols  # Puts everything into a bank 

the_password = random.sample(all_letters, the_length) # .sample basically takes random from a bank a certain amount of times but in an array

final_password = "".join(the_password) # This joins the array contents into one string 

print(final_password)