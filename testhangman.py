import random
import graphics

rand_numb = random.randint(1,64)

def get_random_word():
    text_file = open('words.txt', 'r')
    for i, line in enumerate(text_file):
        if i == rand_numb:
            return "{}".format(line)

secret_word = get_random_word()

print(secret_word) # for testing

secret_word_list = []

def word_list():
    for letter in secret_word:
        secret_word_list.append(letter)

word_list()
secret_word_list = secret_word_list[:-1]
print(secret_word_list)  # for testing

correct_letters = ''

def test_function():
    letter_choice = input("Guess a letter! ")
    if letter_choice not in secret_word_list:
        missed_letters = '' + letter_choice
        print("Sorry!  You have missed a letter {} is not in the secret word.".format(letter_choice))

test_function()
