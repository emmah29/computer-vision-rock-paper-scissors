class rps:

    def play():
        '''
        Plays the rock, paper, scissors game.

        play()
            play()
        '''

        import cv2
        from keras.models import load_model
        import numpy as np
        import random
        import time

        def get_computer_choice():
            '''
            get_computer_choice()
                get_computer_choice()
            
            Gets a choice for the computer. It does this 
            by using a random number generator
            '''
            options = ['Rock', 'Paper', 'Scissors']
            computer_choice = random.choice(options)
            print('The computer chose ' + computer_choice)

            return computer_choice
            
        def get_user_choice():
            '''
            get_user_choice()
                get_user_choice()

            Gets a choice for the user. It does command 
            line input.
            '''
            return input("Rock, Paper, Scissors?")
        
        def get_prediction():
            '''
            get_prediction()
                get_prediction()
            
            Uses the camera to get the user choice
            '''
            model = load_model('keras_model.h5')
            cap = cv2.VideoCapture(0)
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            possible_choices = ['Rock', 'Paper', 'Scissors', 'Nothing']
            start_time = time.time()
            elapsed_time_last_iteration = 0

            while True: 
                ret, frame = cap.read()
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                prediction = model.predict(data,verbose = 0)
                cv2.imshow('frame', frame)
                max_value_in_prediction = prediction[0].max()
                index_of_choice = np.where(prediction[0] == max_value_in_prediction)[0][0]
                
                # Do countdown
                elapsed_time = int(time.time() - start_time)
                if elapsed_time != elapsed_time_last_iteration:
                    if  elapsed_time == 1:
                        print(3)
                    elif elapsed_time == 2:    
                        print(2)
                    elif elapsed_time == 3:    
                        print(1)
                if elapsed_time > 4:
                    break

                elapsed_time_last_iteration = elapsed_time        
            # After the loop release the cap object
            cap.release()
            # Destroy all the windows
            cv2.destroyAllWindows()

            print('You chose ' + possible_choices[index_of_choice])

            return possible_choices[index_of_choice]

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

        computer_wins = 0
        user_wins = 0

        while (computer_wins != 3) and (user_wins != 3):

            Lets_go = input("Press <enter> key to play or x and <enter> to exit")
            if Lets_go == 'x':
                break

            user_choice = get_prediction()
            computer_choice = get_computer_choice()
            result = get_winner(computer_choice, user_choice)
            print(result)
            if result == 'You won!':
                user_wins += 1
            elif result == 'You lost':
                computer_wins += 1
            
            print(f'Score: You {user_wins} Computer {computer_wins}')

        if computer_wins < user_wins:
            print('You won overall')
        else:
            print('You lost overall')

    play()


game = rps
game.play()
