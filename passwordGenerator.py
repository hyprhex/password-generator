import string 

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