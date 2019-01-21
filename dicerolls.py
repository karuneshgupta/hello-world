import random
player1wins=0
player2wins=0

def main():
    player1=0
    player1wins=0
    player2=0
    player2wins=0
    rounds=1

    while rounds!=4:
        print("round"+str(rounds))
        player1=Diceroll()
        player2=Diceroll()
        print("player1 rolls"+str(player1))
        print("player2 rolls"+str(player2))


        if player1==player2:
            print("round draw")
        elif(player1<player2):
            player2wins=player2wins+1
            print("player2 wins the round")
        else:
            player1wins=player1wins+1
            print("player1 wins the round")

        rounds=rounds+1    
if player1wins==player2wins:
        print("all rounds have been drawn")
elif player1wins>player2wins:
        print("player 1 wins and the round wons are " +str(player1wins))
else:
        print("player 2 wins and the round wons are " +str(player2wins))

            


    

def Diceroll():
    diceRoll=random.randint(1,6)
    return diceRoll
main()



