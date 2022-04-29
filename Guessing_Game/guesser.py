import numpy as np
from numpy.core.defchararray import lower



def singleplayer(GUESS,USER):
    ''' 
    Play game with computer. Allows User to guess the number provided by the computer


     PARAMETERS:

     GUESS - Number provided by computer

     ______________________________

     USER - User's attempt to guess the number
    '''
    while SIGNAL == True:

        if USER< GUESS:
            print('Your Guess Was Too Small, Try again')
            SIGNAL == True
            

        elif USER> GUESS:
            print('Your Guess Was Too High Try again')
            SIGNAL == True

        else:
            print("Well Done")
            return SIGNAL == False
        USER = eval(input('Guess the number!\n'))
    return SIGNAL

def multiplayer(GUESS,USER):
    ''' 
    Play game with a friend. Allows Player2 to guess the lucky number provided by Player1
    
    PARAMETERS:

     
    GUESS - Lucky Number provided by computer

     ______________________________

    USER - User's attempt to guess the number
    '''
    while SIGNAL == True:

        if USER< GUESS:
            print('Your Guess Was Too Small, Try again')
            SIGNAL == True
            

        elif USER> GUESS:
            print('Your Guess Was Too High Try again')
            SIGNAL == True

        else:
            print("Well Done")
            return SIGNAL == False
        USER = eval(input('Player2 Guess the number!\n'))
    return SIGNAL

if __name__ == '__main__':
    LOWER_BOUND = 0
    UPPER_BOUND = eval(input('Enter Maximum Number In Range:\n'))
    game_mode = input('Enter Game Mode:\n(Press "s" or single player and "m" for multiplayer \n ')
    game_mode.lower()


 
    SIGNAL = True

    if game_mode == 's':
        GUESS = np.random.randint(LOWER_BOUND,UPPER_BOUND)
        USER = eval(input('Guess the number!\n'))

        singleplayer(GUESS,USER)
    elif game_mode == 'm':
        guess = eval(input("Player1 Enter Lucky Number:\n"))
        USER = eval(input('Player2 Guess the number!\n'))

        multiplayer(guess,USER)
    else:
        print('Enter Correct game mode type')