print("Dice Rolling Simulator")

print("~~~~~~~~~~~~~~~~~~~~")

play_game = input("Do you want to roll the die? (A) Do you want to quit the game? (B) ")
if play_game.lower() == "a":
    import random
    my_number = random.randrange(1,7)
    print("You rolled", my_number, "")
if play_game.lower() == "b":
    import sys
    sys.exit("Game Over")    
        
print("~~~~~~~~~~~~~~~~~~~~")

done = False
while not done:
    play_game = input("Do you want to roll again? ")
    if play_game.lower() == "yes":
        import random
        my_number = random.randrange(1,7)
        print("You rolled", my_number, "")
        
    if play_game.lower() == "no":
        print("You're total number rolled is", my_number, "")
        done = True
        print("Game Over")






#else:
#    print("You're total number rolled is", my_number, "")
    

    

