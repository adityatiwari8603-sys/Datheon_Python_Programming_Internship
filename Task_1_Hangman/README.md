
# 🎮 Hangman Game — Python

## Datheon Python Programming Internship

**Task 1: Terminal-Based Hangman Game**

### 📌 Project Overview

Hangman is an interactive word-guessing game developed using Python.

The program randomly selects a secret word, and the player must guess the correct letters before exhausting six incorrect attempts.

The game displays ASCII Hangman drawings that update after every incorrect guess.

### 🚀 Features

* Random word generation
* Interactive command-line interface
* Six incorrect attempts
* ASCII Hangman visualization
* Correct and incorrect guess detection
* Previously guessed letter tracking
* Duplicate guess protection
* Input validation
* Victory and defeat messages
* Replay functionality
* Graceful keyboard interruption handling

### 🛠 Technologies Used

* Python 3
* Python Standard Library
* `random` module
* Sets, lists, functions, and loops

### 📁 Project Structure

```text
Task_1_Hangman/
│
├── hangman.py
├── README.md
│
└── screenshots/
    └── hangman_game.png
```

### ▶️ How to Run

**Step 1:** Install Python 3.

**Step 2:** Open the project directory.

**Step 3:** Run the following command:

```bash
python hangman.py
```

### 🎯 Game Rules

1. The computer randomly selects a word.
2. The player guesses one letter at a time.
3. Correct letters are revealed in the hidden word.
4. Incorrect guesses reduce the remaining attempts.
5. Duplicate guesses do not reduce attempts.
6. The player wins by guessing every letter.
7. The player loses after six incorrect guesses.

### 💻 Example Output

```text
HANGMAN GAME

A secret word has been selected!
The word contains 6 letters.

Word: _ _ _ _ _ _

Remaining Attempts: 6

Enter a letter: p

Correct! 'P' is in the word.

Word: P _ _ _ _ _
```

### 🧪 Testing

The project is designed to handle:

* Correct letter guesses
* Incorrect letter guesses
* Repeated guesses
* Invalid input
* Winning conditions
* Losing conditions
* Replay requests

### 📚 Concepts Learned

* Python functions
* Conditional statements
* Loops
* Lists and sets
* Random word selection
* String manipulation
* Input validation
* Exception handling

### 🎓 Internship Information

**Organization:** Datheon
**Program:** Python Programming Internship
**Project:** Task 1 — Hangman Game

### 📝 Conclusion

This project demonstrates fundamental Python programming concepts through an interactive terminal-based game. It provides practical experience with control flow, data structures, functions, input validation, and user interaction.
