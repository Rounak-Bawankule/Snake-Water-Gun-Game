# A simple snake water gun

import random

def snake_water_gun():
    """ Funtion for a simple snake water gun game """
    round = 0           # initializing the counter for number of rounds
    computer_score = 0  #initializing the counter for score of computer
    user_score = 0      #initializing the counter for score of user
    while(round<3):
        print("Round - " , round + 1)
        game = ["s" , "w" , "g"]         # List of possible choices to be made by the computer
        comp = random.choice(game)       # computer will have a randon move using the random function
        user = input("Enter your move - (s)snake , (w)water , (g)gun : ")
        print("Computer's move : " , comp)
        print("Users move : ", user)
        if(user == 's' and comp == 's' or user == 'w' and comp == 'w' or user == 'g' and comp == 'g'):
            print("Round Draw! \n Both players get a point")
            round = round + 1
            computer_score = computer_score + 1
            user_score = user_score + 1
        elif(user == 's' and comp == 'w'):
            print("User wins the round")
            round = round + 1
            user_score = user_score + 1
        elif(user == 'w' and comp  == 's'):
            print("Computer wins the round")
            round = round + 1
            computer_score = computer_score + 1
        elif(user == 's' and comp == 'g'):
            print("Computer wins the round")
            round = round + 1
            computer_score = computer_score+1
        elif(user == 'g' and comp == 's'):
            print("User wins the round")
            round = round + 1
            user_score = user_score + 1
        elif(user == 'w' and comp == 'g'):
            print("User wins the round")
            round = round + 1
            user_score = user_score + 1
        elif(user == 'g' and comp == 'w'):
            print("Computer wins the round")
            round = round + 1
            computer_score = computer_score + 1
        else:
            print("please enter valid move")
            snake_water_gun()
    return (computer_score,user_score)

def scores(score_computer , score_user): 
    """ Display winner and score of both players """
    print("The game has ended")
    if(score_computer > score_user ):
        print("Computer has won the game!")
    
    elif(score_user > score_computer):
        print("User has won the game!")
    
    elif(score_user == score_computer):
        print("The score are tied, it's a draw")
    
    print("Scores: \n")
    print("User : ", score_user)
    print("Computer : ", score_computer)

if __name__ == '__main__':
    print("~~~~ Snake-Water-Gun Game~~~~")
    (score_computer,score_user) = snake_water_gun()
        
    scores(score_computer , score_user)     # will call scores function to display results
         
    print("Do you want to play the game again?")
    start = input("Press (s) to play the game again. to quit press (q)")
    if start == 's':
        (score_computer,score_user) = snake_water_gun()
        scores(score_computer , score_user)     # will call scores function to display results
    elif start == 'q':
        exit()
