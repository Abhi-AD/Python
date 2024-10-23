import random


def choose_word():
    words = [
        "python",
        "javascript",
        "java",
        "flutter",
        "react",
        "angular",
        "node",
        "django",
    ]
    return random.choice(words)


def display_word(word, guessed_letters):
    return "".join([letter if letter in guessed_letters else "_" for letter in word])


def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    game_over = False

    while not game_over:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good job! {guess} is in the word.")
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Sorry, {guess} is not in the word.")

        if set(word) <= guessed_letters:
            game_over = True
            print(f"Congratulations! You guessed the word: {word}")
        elif attempts == 0:
            game_over = True
            print(f"Game Over! The word was: {word}")


if __name__ == "__main__":
    hangman()
