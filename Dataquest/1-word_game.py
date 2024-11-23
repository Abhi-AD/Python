import random


def word_guessing_game():
    # Words for the game
    words = ["python", "game", "simple", "fun", "code"]
    word = random.choice(words)  # Randomly select a word
    guessed_word = ["_"] * len(word)
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("Guess the word! You have 6 attempts.")

    while attempts > 0:
        print("\nWord: " + " ".join(guessed_word))
        guess = input("Enter a letter: ").lower()

        # Validate guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Check if guess is correct
        if guess in word:
            print(f"Correct! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Wrong! '{guess}' is not in the word.")
            attempts -= 1

        # Check if the word is fully guessed
        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word:", word)
            return

    print("\nOut of attempts! The word was:", word)


# Save this file as `word_game.py` and run
if __name__ == "__main__":
    word_guessing_game()
