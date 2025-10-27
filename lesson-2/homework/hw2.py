#1
from datetime import date

name = input("What is your name? ")
birth_year = int(input("What year were you born? "))
current_year = date.today().year
age = current_year - birth_year

print(f"Hello, {name}! You are {age} years old.")

#2
txt = 'LMaasleitbtui'

# Hidden pattern: every 2nd letter forms the car name
car_name = txt[::2]
print(car_name) 

#txt = 'MsaatmiazD'

# Let's try every second letter again
car_name = txt[::2]
print(car_name)  # Output: "Mstiz" or maybe backwards?
print(txt[::-2]) # Output: "Daimas" → "Daimas" ≈ "Daimas" (like "Mazda" backwards)


#4
txt = "I'am John. I am from London"

# Extract the word after 'from'
area = txt.split("from ")[1]
print(area)  # Output: London


#5
txt = input("Enter a string: ")
reversed_txt = txt[::-1]
print("Reversed string:", reversed_txt)

#6
txt = input("Enter a string: ").lower()
vowels = "aeiou"
count = sum(1 for char in txt if char in vowels)
print("Number of vowels:", count)

#7
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(n) for n in numbers]
print("Maximum value:", max(numbers))

#8
word = input("Enter a word: ").lower()
if word == word[::-1]:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")

#9
email = input("Enter your email address: ")
domain = email.split('@')[1]
print("Email domain:", domain)

#10
import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

print("Your random password is:", password)
