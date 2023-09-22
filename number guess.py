import random
def play_guess_the_number():
    n = random.randint(1, 100)
    max_turns = 7

    print('Welcome to Guess the Number!')
    print('I have selected a number between 1 to 100.')
    print(f'You have {max_turns} turns to guess it.')

    for turn in range(1, max_turns + 1):
        try:
            guess = int(input(f'Turn {turn}: Enter your guess: '))
        except ValueError:
            print('Invalid input! Please enter a valid number.')
            continue
        if guess < 1 or guess >100:
            print('Please enter a number between 1 and 100.')
            continue
        if guess < n:
            print('Too low! try again.')
        elif guess > n:
            print('Too high! try again')
        else:
            print(f'Congratulations! You guessed the number {n} in {turn} turns')
            break
    else:
        print('Game Over! The number was {n}.')
    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() =='yes' or play_again.lower() == 'y':
        play_guess_the_number()
    else:
        print('Thanks for playing!')
if __name__ =="__main__":
    play_guess_the_number()

   
