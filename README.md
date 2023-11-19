# hangman
A Python-based implementation of the classic Hangman game.

Hangman Game in Python

Introduction

Welcome to the Hangman game implemented in Python! This console-based game challenges players to guess a secret word within a limited number of attempts. The game randomly selects a word from various categories, and players must guess individual letters to uncover the hidden word. Be careful—six incorrect guesses will lead to failure!


Features

Categories: Choose from a variety of word categories for an added challenge.
Visual Feedback: Enjoy ASCII art depicting the progress of a hanging man with each incorrect guess.
User-Friendly Interface: Receive clear prompts for letter inputs and game outcomes.
Setup
Ensure you have Python installed on your machine.
Clone or download the Hangman code.
Open a terminal or command prompt and navigate to the directory containing the code.
Run the game by executing the command: python hangman.py (replace "hangman.py" with the actual filename if needed).
Functionality
1. read_categories(file_path)
Reads categories from a file and returns a dictionary where each category maps to a list of words.

2. choose_word(category)
   Chooses a random word from the given category.

3. print_categories(categories)
   Prints the available categories.

4. select_random_word(file_path)
   Selects a random word from a random category, prompting the user to choose a category.

5. number_of_letters(word)
   Displays the number of letters in the secret word.

6. is_valid_input(choice, old_letters)
   Checks if the user's input is a valid single letter.

7. show_hidden_word(secret_word, old_letters_guessed)
   Updates the appearance of the secret word based on guessed letters.

8. try_update_letter_guessed(choice, letter_list)
   Updates the list of guessed letters.

9. check_win(secret_word, old_letters_guessed)
   Checks if the player has guessed all the letters correctly.

10. print_hangman(num_of_tries)
    Prints the state of the hanging man based on the number of incorrect attempts.


Main Code
The main code initiates the game, allowing players to guess letters and providing feedback until they either win or reach the maximum number of failed attempts. Players can choose to play again or exit the game.

Enjoy playing Hangman! 🎮

