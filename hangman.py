from random import choice

def run_game():
    word: str = choice(['apple', 'secret','banana'])

    username: str = input('What is your name? >> ')
    print(f'Welcome to hangman, {username}!')

    #setup
    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('word: ', end ='')

        for char in word:
            if char in guessed:
                print(char,end ='')
            else:
                print('_', end ='')
                blanks += 1

        print() #adds a blank line

        if blanks == 0:
            print('You got it')
            break
        guess: str = input('Enter a letter:')

        if guess in guessed:
            print(f'you already used: "{guess}". Please try with another letter!')
            continue

        guessed += guess

        if guess not in word:
           tries -= 1
           print(f'Sorry, that was wrong ... ({tries} tries remaining)')

           if tries == 0:
               print('No more tries remaining ...you lose.')
               break
if __name__ =='__main__':
    run_game()