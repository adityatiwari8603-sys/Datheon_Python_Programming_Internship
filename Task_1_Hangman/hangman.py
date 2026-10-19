"""
DATHEON PYTHON PROGRAMMING INTERNSHIP

Task 1: Hangman Game

Description:
A terminal-based word guessing game.
The player must guess the hidden word
before making six incorrect guesses.

Author: Internship Student
"""

import random


# List of words used in the game
WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard",
    "internet",
    "software",
    "algorithm",
    "database",
    "function",
    "variable",
    "technology",
    "education",
    "learning",
    "project"
]


# Maximum number of incorrect guesses
MAX_ATTEMPTS = 6


# ASCII Hangman drawings
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def display_welcome():
    """Display the welcome screen."""

    print("\n" + "=" * 50)
    print("             HANGMAN GAME")
    print("=" * 50)

    print("\nWelcome to the Hangman Game!")

    print("\nGame Rules:")
    print("1. A random word will be selected.")
    print("2. Guess one letter at a time.")
    print("3. You have 6 incorrect attempts.")
    print("4. Correct guesses reveal hidden letters.")
    print("5. Repeated guesses do not reduce attempts.")

    print("\nGood luck!")
    print("=" * 50)


def choose_word():
    """Choose a random word from the list."""

    return random.choice(WORDS)


def display_word(secret_word, guessed_letters):
    """Display correctly guessed letters."""

    displayed_word = []

    for letter in secret_word:

        if letter in guessed_letters:
            displayed_word.append(letter.upper())

        else:
            displayed_word.append("_")

    return " ".join(displayed_word)


def get_guess(guessed_letters):
    """Get a valid letter from the player."""

    while True:

        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue

        if not guess.isascii() or not guess.isalpha():
            print("Only English alphabet letters are allowed.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            print("Try another letter.")
            continue

        return guess


def check_win(secret_word, guessed_letters):
    """Check whether every letter has been guessed."""

    return all(
        letter in guessed_letters
        for letter in secret_word
    )


def play_game():
    """Run one complete Hangman game."""

    secret_word = choose_word()

    guessed_letters = set()

    incorrect_guesses = 0

    print("\nA secret word has been selected!")
    print(f"The word contains {len(secret_word)} letters.")

    while incorrect_guesses < MAX_ATTEMPTS:

        print(HANGMAN_STAGES[incorrect_guesses])

        print(
            "Word:",
            display_word(secret_word, guessed_letters)
        )

        print(
            f"\nRemaining Attempts: "
            f"{MAX_ATTEMPTS - incorrect_guesses}"
        )

        if guessed_letters:
            print(
                "Guessed Letters:",
                ", ".join(sorted(guessed_letters))
            )

        else:
            print("Guessed Letters: None")

        guess = get_guess(guessed_letters)

        guessed_letters.add(guess)

        if guess in secret_word:

            print(f"\nCorrect! '{guess.upper()}' is in the word.")

        else:

            incorrect_guesses += 1

            print(f"\nWrong! '{guess.upper()}' is not in the word.")

        if check_win(secret_word, guessed_letters):

            print("\n" + "=" * 50)
            print("             YOU WIN!")
            print("=" * 50)

            print(f"\nCongratulations!")
            print(f"You guessed the word: {secret_word.upper()}")

            print(
                f"Incorrect Guesses: "
                f"{incorrect_guesses}/{MAX_ATTEMPTS}"
            )

            return

    # Game over
    print(HANGMAN_STAGES[MAX_ATTEMPTS])

    print("\n" + "=" * 50)
    print("             GAME OVER!")
    print("=" * 50)

    print("\nYou have used all 6 incorrect attempts.")

    print(f"The correct word was: {secret_word.upper()}")

    print("\nBetter luck next time!")


def main():
    """Main function to start and replay the game."""

    display_welcome()

    while True:

        play_game()

        while True:

            replay = input(
                "\nWould you like to play again? (yes/no): "
            ).strip().lower()

            if replay in ["yes", "y"]:
                break

            elif replay in ["no", "n"]:
                print("\nThank you for playing Hangman!")
                print("Goodbye!")
                return

            else:
                print("Invalid choice! Please enter yes or no.")


if __name__ == "__main__":
    try:
        main()

    except (KeyboardInterrupt, EOFError):
        print("\n\nGame interrupted. Goodbye!")