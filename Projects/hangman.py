#hangman without visual and everything just figuring out basics
import random as r
print('Welcome to Hangman!')
print('------------------------------')
words = ['quick', 'overt','report', 'holistic', 'save', 'four', 'tranquil', 'teaching', 'ludicrous', 'tacky' ,'entertain','load', 'allow', 
'home', 'ratty', 'careless','discover', 'finicky', 'spell', 'women', 'serious', 'hose', 'amazing', 'banana', 'dinosaur', 'super', 'drink']
random_word = r.choice(words)
for x in random_word:
    print('_', end=' ')

def print_hangman(wrong):
    if wrong == 0:
        print('\n+---+')
        print('    |')
        print('    |')
        print('    |')
        print('   ===')
    elif wrong == 1:
        print('\n+---+')
        print(' O  |')
        print('    |')
        print('    |')
        print('   ===')
    elif wrong == 2:
        print('\n+---+')
        print(' O  |')
        print(' |  |')
        print('    |')
        print('   ===')
    elif wrong == 3:
        print('\n+---+')
        print(' O  |')
        print('/|  |')
        print('    |')
        print('   ===')
    elif wrong == 4:
        print('\n+---+')
        print(' O  |')
        print('/|\ |')
        print('    |')
        print('   ===')
    elif wrong == 5:
        print('\n+---+')
        print(' O  |')
        print('/|\ |')
        print('/   |')
        print('   ===')
    elif wrong == 6:
        print('\n+---+')
        print(' O  |')
        print('/|\ |')
        print('/ \ |')
        print('   ===')

def print_word(guessed_letters):
    counter = 0
    correct_letters = 0
    for char in random_word:
        if char in guessed_letters:
            print(random_word[counter], end=' ')
            correct_letters += 1
        else:
            print(' ', end=" ")
        counter += 1
    return correct_letters