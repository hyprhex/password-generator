import string, random

lower_alphabet_character = list(string.ascii_lowercase)
upper_alphabet_character = list(string.ascii_uppercase)
digit_character = list(string.digits)
punctuation_character = list(string.punctuation)

user_input = input("How many character you want for your password: ")

while True:
    try:
        user_input = int(user_input)
        if user_input < 6:
            print("You need at least 6 characters")
            user_input = input("Enter your password character: ")
        else:
            break
    except:
        print("Password character must be only numbers")
        user_input = input("How many character you want for your password: ")

random.shuffle(lower_alphabet_character)
random.shuffle(upper_alphabet_character)
random.shuffle(digit_character)
random.shuffle(punctuation_character)

# 30% of the first half 
first_half = round(user_input * (30/100))

# 20% of the second half
second_half = round(user_input * (20/100))

password = []

for i in range(first_half):
    password.append(lower_alphabet_character[i])
    password.append(upper_alphabet_character[i])

for i in range(second_half):
    password.append(digit_character[i])
    password.append(punctuation_character[i])