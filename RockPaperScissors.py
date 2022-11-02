import random as r

def game():
    player = input("Type 'R' for Rock, 'P' for paper, 's' for scissors: ").lower()
    computer = r.choice(['r', 'p', 's'])

    # p > r, r > s, s > p
    

    
    while player != computer:
        
        if (player == 'p' and computer == 'r' ) or (player == 'r' and computer == 's') \
        or (player == 's' and computer == 'p'):
            print( f'Player won the match, computer {computer}')
            break
        elif (computer == 'p' and player == 'r' ) or (computer == 'r' and player == 's') \
        or (computer == 's' and player == 'p'):
            print( f'Computer won the match {computer}')
            break

    else: print( f'Tie {computer}')

print(game())

    