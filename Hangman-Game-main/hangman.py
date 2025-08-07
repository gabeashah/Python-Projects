from words import word_list 
import random
import time

# Hangman Game

# countdown function to show a loading piece before the game starts
# It will print "Loading Hangman..." and then count down from 3 to 1
# with a 1 second pause between each number.
# After the countdown, it will print "Let's start!" to indicate the game is ready to begin.
def countdown():
    print("Loading Hangman...", end="", flush=True)
    for i in range(3, 0, -1):
        print(f" {i}", end="", flush=True)
        time.sleep(1)
    print("\nLet's start!\n")

# get_word is a function that randomly slects a word from the list of words.
# It uses the random.choice() function to select a word from the word_list.
# The selected word is then converted to uppercase to maintain consistency in the game.
def get_word():
    word = random.choice(word_list)
    return word.upper()

# display_hangman is a function that takes the number of tries left as an argument
# it is also responsible for displaying the current state of the hangman.
def display_hangman(tries):
    stages = [
        """
        -----
        |   |
        |   O
        |  /|\\
        |  / \\
        -
        """,
        """
        -----
        |   |
        |   O
        |  /|\\
        |  /
        -
        """,
        """
        -----
        |   |
        |   O
        |  /|
        |
        -
        """,
        """
        -----
        |   |
        |   O
        |   |
        |
        -
        """,
        """
        -----
        |   |
        |   O
        |
        |
        -
        """,
        """
        -----
        |   |
        |
        |
        |
        -
        """,
        """
        -----
        
        
        
        
        
        """,
    ]
    return stages[tries]

# play is the main function that runs the game.
# It initializes the game state, including the word to guess, the number of tries,
# and the lists for guessed letters and words.
# It then enters a loop where the player can guess letters or the entire word.
# The game continues until the player either guesses the word or runs out of tries.
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Lets play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n") 
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed that letter. Try again.")
            elif guess not in word:
                print("Sorry, that letter is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job, that letter is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed that word. Try again.")
            elif guess != word:
                print("Well you guessed something. That word is not correct. Try again")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Better luck next time!")

# main function to start the game
# It prompts the user for their name, asks if they are ready to play,
# and starts the countdown before beginning the game.
# After the game ends, it asks if the user wants to play again.
def main(user_name=None):
    if user_name is None:
        print("Welcome to Hangman!")
        user_name = input("What is your name? ")
        print(f"Hello {user_name} welcome to the game!")
    start_game = input("Are you ready to play? Y/N: ")

    if start_game.upper() == "Y":
        print("Great! Let's get started!")
    else:
        print("Okay, maybe next time!")
        return
    countdown()
    print("The game is starting now!")
    print("You have 6 tries to guess the word.")
    print("You can guess a letter or the entire word.")
    print("Good luck!")
    print("Here is the word you need to guess:")
    print("_________________________")
    word = get_word()
    play(word)

    print("Do you want to play again? Y/N")
    play_again = input().upper()
    if play_again == "Y":
        print("Awesome! Let's play again!")
        main(user_name)
        
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
