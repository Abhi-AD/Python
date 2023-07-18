import random

def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter.lower() in vowels

def is_consonant(letter):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    return letter.lower() in consonants

def main():
    random_letter = random.choice('abcdefghijklmnopqrstuvwxyz')    
    user_input = input("Enter a letter: ").upper()
    
    if len(user_input) != 1:
        print("Please enter a single letter.")
        return
    
    if is_vowel(user_input):
        print(user_input, "is a vowel!")
    elif is_consonant(user_input):
        print(user_input, "is a consonant!")
    else:
        print("Invalid input.")

if __name__ == '__main__':
    main()
