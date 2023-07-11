def play():
    '''
    Plays the rock, paper, scissors game.
    '''

    import random

    def get_computer_choice():
        '''
        get_computer_choice()
            get_computer_choice()
        
        Gets a choice for the computer. It does this 
        by using a random number generator
        '''
        options = ['Rock', 'Paper', 'Scissors']
        return random.choice(options)
        
    def get_user_choice():
        '''
        get_user_choice()
            get_user_choice()

        Gets a choice for the user. It does command 
        line input.
        '''
        return input("Rock, Paper, Scissors?")

    def get_winner(computer_choice, user_choice):
        '''
        get_winner()
            get_winner(computer_choice, user_choice)
        
        Determines who the winner is using the 
        conventional rock paper scissors rules. 

        computer_choice String One of Rock, Paper, Scissors
        user_choice String One of Rock, Paper, Scissors
        '''
        if computer_choice != user_choice:
            if computer_choice == 'Rock' and user_choice == "Paper":
                return 'You won!'
            elif computer_choice == 'Paper' and user_choice == "Scissors":
                return 'You won!'
            elif computer_choice == 'Scissors' and user_choice == "Rock":
                return 'You won!'
            else:
                return 'You lost'
        else:
            return 'It was a draw'

    computer_choice = get_computer_choice()
    print(computer_choice)
    user_choice = get_user_choice()
    print(get_winner(computer_choice, user_choice))

play()
