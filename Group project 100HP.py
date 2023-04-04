
import random
#class named Player that uses the constructor method init
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
#
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

#Sources: https://www.sololearn.com/compiler-playground/c4k4Z0UNP4Cc/
# https://codereview.stackexchange.com/questions/205440/2-player-dice-game