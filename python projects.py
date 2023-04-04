# Define the Player class
import random
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





