import random
import graphics

rand_numb = random.randint(1,64)

def get_random_word():
    text_file = open('words.txt', 'r')
    for i, line in enumerate(text_file):
        if i == rand_numb:
            return "{}".format(line)

secret_word = get_random_word()

#print(secret_word)

secret_word_list = []

def word_list():
    for letter in secret_word:
        secret_word_list.append(letter)

word_list()
secret_word_list = secret_word_list[:-1]
#print(secret_word_list)



def main():
    print('H A N G M A N')
    missed_letters = ''
    correct_letters = ''
#   secret_word = get_random_word()
#    secret_word_list = secret_word.split()
    game_is_done = False
    while True:
        graphics.display_board(missed_letters, correct_letters, secret_word) #<- make sure these variables align
        letter_choice = input("Guess a letter! ")
        if letter_choice in secret_word_list:
            correct_letters += '' + letter_choice
            print("Correct! {} is in the in the secret word!".format(letter_choice))
            if len(correct_letters) == len(secret_word):
                print("Congratulations!  You won.")
                return None
        else:
            missed_letters += '' + letter_choice
            print("Sorry!  You have missed a letter {} is not in the secret word.".format(letter_choice))
            if len(missed_letters) == 7:
                print("Oh no!  You have missed 7 letters.  The game is over")
                return None
def again():
    while True:
        try:
            play_again = input("Would you like to play again? y/n ").lower()
            if play_again == "y":
                main()
            else:
                print("Thank you for playing!")
                return None
        except:
            print("That is not a valid entry. Please try again.")
            return None

main()
again()
# Check if the player has won
# Check if player has guessed too many times and losttest
#print letter in correct spot
# Ask the player if they want to play again (but only if the game is done).
#if letter_choice not in secret_word_list:
