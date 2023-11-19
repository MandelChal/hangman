import random
import sys
import re

FAILED_ATTEMPTS = 6
HANGMAN_PHOTOS = 0
old_letters = []
again = True

HANGMAN_ASCII_ART = """\n HI! \n Welcome to the game Hangman!😊
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/     
\n"""


def read_categories(file_path):

    # Read categories from a file and return a dictionary where each category
    # maps to a list of words.
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    categories = {}
    current_category = None

    for line in lines:
        line = line.strip()
        if line.endswith(':'):
            current_category = line[:-1]
            categories[current_category] = []
        elif current_category is not None:
            categories[current_category].append(line)

    return categories


def choose_word(category):
    #Choose a random word from the given category.
    return random.choice(category)


def print_categories(categories):
    #Print the available categories.
    print("\n Available categories:")
    for i, category in enumerate(categories, start=1):
        print("", f"{i}. {category}")


def select_random_word(file_path):
    #Select a random word from a random category.
    categories = read_categories(file_path)
    print_categories(categories)

    try:
        choicen_category_index = int(input("\n Choose the number of the category: "))
        choicen_category = list(categories.keys())[choicen_category_index - 1]

        selected_word = choose_word(categories[choicen_category])
        return choicen_category, selected_word

    except (ValueError, IndexError):
        print(" Invalid input. Please enter a valid category number.")
        return None, None


def number_of_letters(word):
    #Display the number of letters in the secret word.
    length = len(word)
    underscores = ' _' * length
    print("", underscores)
    print("\n")


def is_valid_input(choice, old_letters):
    #Check if the user's input is valid.
    if len(choice) == 1:
        har_code = ord(choice)

        if (65 <= har_code <= 90) or (97 <= har_code <= 122):
            choice = choice.lower()
            for letter in old_letters:
                if choice == letter:
                    print(" old letter")
                    try_update_letter_guessed(choice, old_letters)
                    return False

            return True

        else:
            return False

    else:
        english_letters_pattern = re.compile(r'[a-zA-Z]')
        input_string = choice

        if english_letters_pattern.search(input_string) and not input_string.isalpha():
            return False

        else:
            return False


def show_hidden_word(secret_word, old_letters_guessed):
    #Update the appearance of the secret word.
    display_list = []
    for char in secret_word:
        if char in old_letters_guessed:
            display_list.append(char)
        else:
            display_list.append('_ ')

    display_string = ' '.join(display_list)
    print("\n The secret word:\n", display_string)


def try_update_letter_guessed(choice, letter_list):
    #Update the list of guessed letters.
    sorted_letters = sorted(letter_list, key=lambda x: x.upper())
    print(" The list of guessed letters:", ' -> '.join(sorted_letters))


def check_win(secret_word, old_letters_guessed):
    #Check if the player has guessed all the letters correctly.
    result = all(letter in old_letters_guessed for letter in secret_word)
    return result


def print_hangman(num_of_tries):
    #Print the state of the hanging man.
    hangman_dict = {
        0: " x-------x",
        1: "\n x-------x\n |\n |\n |\n |\n |",
        2: "\n x-------x\n |       | \n |       0\n |\n |\n |",
        3: "\n x-------x\n |       | \n |       0\n |       |\n |\n |",
        4: "\n x-------x\n |       | \n |       0\n |      /|\\ \n |\n |",
        5: "\n x-------x\n |       | \n |       0\n |      /|\\ \n |      /\n |",
        6: "\n x-------x\n |       | \n |       0\n |      /|\\ \n |      / \\ \n |"
    }

    print("\n The number of failures so far:", num_of_tries, "\n")

    if num_of_tries in hangman_dict:
        print(hangman_dict[num_of_tries], "\n")
    else:
        print(" Invalid number of tries")


while again:
    old_letters.clear()
    HANGMAN_PHOTOS = 0
    print(HANGMAN_ASCII_ART, "The number of possible failures:", FAILED_ATTEMPTS)
    random_word = select_random_word(r"C:\Users\User\Desktop\VS_code\python\hangMan_categories.txt")
    if random_word[0] and random_word[1]:
        print(f" Randomly selected word from {random_word[0]}")

    secret_word = random_word[1]
    #print(random_word[1])-->secret_word
    number_of_letters(secret_word)
    error = print_hangman(HANGMAN_PHOTOS)

    while True:
        choice = input(" Type a character: ")
        valid_choice = is_valid_input(choice, old_letters)
        while not valid_choice:
            print("\n")
            choice = input(" Invalid,Please enter a one-word string again: ")
            valid_choice = is_valid_input(choice, old_letters)

        if valid_choice:
            choice = choice.lower()
            old_letters.append(choice)
            try_update_letter_guessed(choice, old_letters)
            if choice in secret_word:
                show_hidden_word(secret_word, old_letters)
                print("\n")
                win = check_win(secret_word, old_letters)
                if win:
                    print(" you win! 🎉")
                    print(" The secret word is:", secret_word, "\n")
                    break

            else:
                HANGMAN_PHOTOS += 1
                print("")
                show_hidden_word(secret_word, old_letters)
                print_hangman(HANGMAN_PHOTOS)
                if HANGMAN_PHOTOS == 6:
                    print(" You failed, but that's okay, maybe you'll succeed next time! 🙂")
                    print(" The secret word is:", secret_word, "\n")
                    break

    newGame = input(" Play again? \n Y for Yes  \n Q to Quit  \n\n")
    if newGame.lower() == 'y':
        print(" 💖💖💖")
        print(" Let's start playing again!")
        continue

    else:
        print(" 💗💗💗")
        print(" Thank you for playing!\n")
        again == False
        sys.exit(" Bye! 👏\n")
