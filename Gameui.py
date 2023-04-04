import tkinter as tk
import sys
import random

def start_game1(): #Game 1
#Romano James(1908909)
    def MyGame():
        #Define the lose class
        def lose1():
            print ("\n\nYOU LOSE !")
            print("Better luck next time !")
            exit(0)
        #check if the numbers are sequential    
        def check(xyz):
            i = 1
            while i<len(xyz):
                if (xyz[i]-xyz[i-1])!= 1:
                    return False
                i = i + 1
            return True

         #the start function
        def start1():
            xyz = []
            last = 0
            while True:
                print ("Enter 'F' to Proceed.")
                chance = input('> ')
                 
                # player takes the first chance
                if chance == "F":
                    while True:
                        if last == 20:
                            lose1()
                        else:
                            print ("\nYour Turn.")
                            print ("\nHow many numbers do you wish to enter?")
                            inp = int(input('> '))
                             
                            if inp > 0 and inp <= 3:
                                comp = 4 - inp
                            else:
                                print ("Wrong input. You are disqualified from the game.")
                                lose1()
                     
                            i, j = 1, 1
         
                            print ("Now enter the values")
                            while i <= inp:
                                a = input('> ')
                                a = int(a)
                                xyz.append(a)
                                i = i + 1
                             
                            # store the last element of xyz.
                            last = xyz[-1]
                             
                            # checks whether the input
                            # numbers are consecutive
                            if check(xyz) == True:
                                if last == 21:
                                    lose1()
                                     
                                else:
                                    #Computer's turn.
                                    while j <= comp:
                                        xyz.append(last + j)
                                        j = j + 1
                                    print ("Order of inputs after computer's turn is: ")
                                    print (xyz)
                                    last = xyz[-1]
                            else:
                                print ("\nYou did not input consecutive integers.")
                                lose1()
        #the game function
        def play_game():
            player_score = 0
            while player_score < 21:
                num = random.randint(1, 21)
                print("Random number generated: ", num)
                if num % 2 == 0:
                    player_score += num
                    print("Your score is now: ", player_score)
                else:
                    player_score -= num
                    print("Your score is now: ", player_score)
            if player_score == 21:
                print("Congratulations! You won!")
            else:
                print("Sorry, you lost.")
            while player_score <21:
                continue
        #initializes the game    
        game = True   
        while game == True:
            print ("Player 2 is Computer.")
            print("Do you want to play the 21 number game? (Yes / No)")
            ans = input('> ')
            if ans =='Yes':
                play_game(start1())
            else:
                print ("Do you want quit the game?(yes / no)")
                nex = input('> ')
                if nex == "yes":
                    print ("You are quitting the game...")
                    exit(0)
                elif nex == "no":
                    print ("Continuing...")
                else:
                    print ("Wrong choice")
                        
    MyGame()
    
def start_game2(): #Game 2
#Shaquille Ford (2207724)
    def MyGame2():
        class Player:
            def __init__(self, name):
                self.name = name
                self.position = 0

            
            def roll_dice(self):
                diceRoll = random.randint(1, 6)
                return diceRoll
        # Define the game function
        def play_game():
        # Initialize players
            num_players = int(input("Enter the number of players: "))
            players =[Player(input(f"Enter player {i+1}'s name: ")) for i in range(num_players)]
        #def play_game():
            winner=100
            while winner==100:
                for player in players:
                    print(f"{player.name}, it's your turn.")
                    input("Press enter to roll the dice...")
                    roll = player.roll_dice()
                    print(f"You rolled a {roll}.")
                  # Update player's position
                    
                     
        #Check for dice game
                    if roll % 2 == 0:
                        player.position =player.position + roll
                        print(player.name,"Your position as increase,you are at position:",player.position)
                    
                    elif roll % 2 != 0:
                        player.position =player.position - roll
                        print(player.name,"Your position as decrease,you are at position:",player.position)
           
                    if player.position < 0:
                        player.position=0
                        print("Opps ",player.name," your position have fallen below 0,your position has been corrected to:",player.position)
                    
                   # Check if the player has won  
                    if player.position >= 50:
                        winner = player.name
               
                        print(f"You are now on position {player.position}.\n")

         # Print the winner
                        print(f"Congratulations, {winner.name}! You won the game.")

        # Call the game function
        play_game()   
    MyGame2()
    
def start_game3(): #Game 3
#Trey Johnson 2207508 RPG GAME    
    def MyGame3():
        #class named Player that uses the constructor method init
        class Player:
            def __init__(self, name):
                self.name = name
                self.health = 100
                
            def take_damage(self, damage):
                self.health -= damage
        #The numbers that can be rolled are 1-6 therefore the maximum amout fo damage that can be given/recived is 6 and the minimum is 1
            def roll_dice(self): 
                return random.randint(1,6)


        def main():
                # Input player names/ Players one and two are prompted to input their names
                player1_name = input("PLAYER 1 ENTER YOUR NAME !!! \U00002B1B : ")
                player2_name = input("PLAYER 2 ENTER YOUR NAME !!! \U00002B1C: ")

                # Creation of player objects. This establishes 2 players 
                player1 = Player(player1_name)
                player2 = Player(player2_name)

                # Game loop/ Starts the loop 
                while player1.health > 0 and player2.health > 0 :
                    # Player 1's turn to roll
                    input(f" \U00002B1B {player1.name}, PRESS ENTER TO ROLL THE DICE !!!.")
                    roll = player1.roll_dice()
                    player2.take_damage(roll)
                    print(f"{player1.name} ROLLED {roll} AND HIT \U0001F91C {player2.name} FOR {roll} DAMAGE!!!")
                    print(f"{player2.name} IS NOW ON {player2.health}HP")
            #the loop ends when either player 1 or 2 has health below or equal to 0
                    if player2.health <= 0:
                        break

                    # Player 2's turn to roll
                    input(f"\U00002B1C {player2.name},  PRESS ENTER TO ROLL THE DICE !!")
                    roll = player2.roll_dice()
                    player1.take_damage(roll)
                    print(f"{player2.name} ROLLED {roll} AND HIT \U0001F91C {player1.name} FOR {roll} DAMAGE!!!")
                    print(f"{player1.name} IS NOW ON {player1.health}HP")

                # Game over,the winner is determined by the player with 0 or less health 
               # when that is determined there will be an output that reads one of the following 
                if player1.health <= 0:
                    print(f"{player2.name} HAS BEEN DEFEATED {player1.name} WINS!!!")
                else:
                    print(f"{player1.name} HAS BEEN DEFEATED {player2.name} WINS!!")


        if __name__ == '__main__':
                    main()
            #initalizes the game menu
    MyGame3()
    
root = tk.Tk()
root.title("Game Menu")

start_button = tk.Button(root, text="Start the 21 Game by Romano", command=start_game1)
start_button.pack()
start_button = tk.Button(root, text="Start the Dice Roll Game by Shaquille", command=start_game2)
start_button.pack()
start_button = tk.Button(root, text="Start the RPG Game by Trey", command=start_game3)
start_button.pack()
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()