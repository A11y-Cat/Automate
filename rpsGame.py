import random,sys

#Rock paper scissors game

print("ROCK PAPER SCISSORS")
print (" ")

#keeping track of the score

win = 0
loss = 0
draw = 0

        
while True: # The main game loop.
    print('%s Win, %s Loss, %s Draw' % (win, loss, draw))
    print(" ")
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        print(" ")
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')
        
    #Diplays players move:
        
    if playerMove == 'r':
        print(" ")
        print("Rock versus.. ")
    elif playerMove == 'p':
        print(" ")
        print("Paper versus.. ")
    elif playerMove == 's':
        print(" ")
        print("Scissors versus.. ")
        
    #displays computers move:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print("Rock")
    elif randomNumber == 2:
        computerMove = 'p'
        print("Paper")
    elif randomNumber == 3:
        computerMove = 's'
        print("Scissors")
        
    #Display result, count scores
    
    if playerMove == computerMove:
        print("It's a draw!")
        draw = draw + 1
    elif playerMove == 'r' and computerMove == 's':
        print("You win!")
        win = win +1
    elif playerMove == 'r' and computerMove == 'p':
        print("You lose!")
        loss = loss + 1
    elif playerMove == 's' and computerMove == 'r':
        print("You lose!")
        loss = loss + 1
    elif playerMove == 's' and computerMove == 'p':
        print("You win!")
        win = win + 1
    elif playerMove == 'p' and computerMove == 'r':
        print("You win!")
        win = win + 1
    elif playerMove == 'p' and computerMove == 's':
        print("You lose!")
        loss = loss + 1
        