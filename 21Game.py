#Romano James 21 Game
import random

def lose1():
    print ("\n\nYOU LOSE !")
    print("Better luck next time !")
    exit(0)
    
def check(xyz):
    i = 1
    while i<len(xyz):
        if (xyz[i]-xyz[i-1])!= 1:
            return False
        i = i + 1
    return True
 
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
                
