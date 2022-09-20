import random
import string

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

all_combinations = lower_letters + upper_letters + numbers + symbols

password_length = 12

password = ''.join(random.sample(all_combinations, password_length))

print(password)
