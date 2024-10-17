
import numpy as np
import Movement
import BoardDisp

Dimension = 7

NumFortress = 3

Game_over = False

Turn_dict = {2: 1, 1: 2}

print('\n\n ~<>~ ~<>~ ~<>~ ~<>~ FORTRESS ~<>~ ~<>~ ~<>~ ~<>~ ~<>~')
print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . ')
print(' . . . . . . . . . . . . ,-,_,-,_,-,_,-,_,-,_,-, . . . .')
print('. . . . . . . . . . . . .|___|___|___|___|___|_|. . . . ')
print(' . . . . . . . . . . . . |_|___|___|___|___|___| . . . .')
print('. . . . . . . . . . . . . .\\_|___|___|___|___/. . . . . ')
print('_==_ . . ,---, . . . . . . .|___|___|___|___|. . . . . .')
print('\\__/====/ /O\\ \\===. . . . . |_|___/   \\___|_| . . . . . ')
print(' . . . / / . \\ \\ . . . . . .|__|_|     |_|__|. . . . . .')
print('. ____/_/_____\\_\\_. . . . . |_|__|     |__|_| . . . . . ')
print(' .\'=O============O\'. . . . /_|___|_____|___|_\\.  . . . .')
Load = 0


''' LOADING OR NEW GAME '''

while Load != 'L' and Load != 'N':
    
    #user chooses whether to start a new game or load a previous game save
    
    Load = input('>> Load or Start New? (L/N) <<\n\n')     
    
            
    if Load != 'L' and Load != 'N':
                
        print('\nError, you must choose either Load \'L\' or Start New \'N\'')

if Load == 'L': #if user chose to load a game
    
    saveData = 'initial string'
    
    while type(saveData) == str: 
        
        #uses the load function to load a desired save
        
        saveData = BoardDisp.load()
        
        if type(saveData) == str:            
            print(saveData) #if the load fails, the load function will return a string that specifies the error. This prints the error
    
    
    if type(saveData) != bool: #saveData will be False when no saves are available
        
        #assigning the save file data to variables
        
        Board_pieces = saveData[0]
        Board_power = saveData[1]
        Player_powerpieces = saveData[2]
        Turn_order = saveData[3]   
        
        BoardDisp.display(Board_pieces, Board_power, Player_powerpieces)
    
    else:
        print('\nNo saves avilable! Will now start a new game.\n')
    
    
if Load == 'N' or type(saveData) == bool:
    
    #initializing the variables for the location of playing pieces and their power
    
    Board_pieces = np.array([[3,1,1,0,2,2,4],
                        [1,1,1,0,2,2,2],
                        [1,1,1,0,2,2,2],
                        [3,1,1,0,2,2,4],
                        [1,1,1,0,2,2,2],
                        [1,1,1,0,2,2,2],
                        [3,1,1,0,2,2,4]])


    Board_power = np.array([[1,2,1,0,1,2,1],
                       [2,2,1,0,1,2,2],
                       [2,2,1,0,1,2,2],
                       [1,2,1,0,1,2,1],
                       [2,2,1,0,1,2,2],
                       [2,2,1,0,1,2,2],
                       [1,2,1,0,1,2,1]])


    Player_powerpieces = [0,0] #stores the amount of power pieces for each player
    
    Turn_order = 1 #dictates the turn order
    
    BoardDisp.display(Board_pieces, Board_power, Player_powerpieces) #sends the board state data to the displaying function which will display it on the terminal



'''MAIN GAME'''


while not Game_over:   

    
    '''MOVE OR DEPLOY CHOICE'''
    
    Turn_choice = 0
    
    if Movement.deploy_check(Board_pieces, Turn_order) == False or Player_powerpieces[Turn_order-1] == 0: #checks if the player can perform a "deploy" move
        
        Turn_choice = 'M' #if the player cannot deploy, the player must move "M"
    
    
    while Turn_choice != 'M' and Turn_choice != 'D': 
        
        #player choses to either deploy or move
        
        print('\nPlayer', Turn_order,', what would you like to do this turn? (Move \'M\'/Deploy \'D\'):')        
        
        Turn_choice = input('')
            
        if Turn_choice != 'M' and Turn_choice != 'D':
                
            print('\nError, you must choose either Move \'M\' or Deploy \'D\'')    
    
    
    
    ''' DEPLOY '''
    
    
    if Turn_choice == 'D': #if the player decides to deploy
        
        Board_state = 'initial string'
        
        while type(Board_state) == str:
            
            print('\nPlayer', Turn_order,', where to deploy? (ex.: a1) (or type \'save\' or \'end\'):') #player choses when to deploy (they can also end or save the game)
            
            Deploy_location = input('')

 
            '''END OR SAVE'''
           
            if Deploy_location == 'end': #when ending the game, the program ends and declares no one is the winner
                winner = 'no one'
                break
            
            if Deploy_location == 'save': #when saving the game, the board state is save using the save function           
                
                BoardDisp.save(Board_pieces, Board_power, Player_powerpieces, Turn_order)                
                winner = 'undecided'
                break
                      
            
            Board_state = Movement.deploy(Board_pieces, Board_power, Deploy_location, Player_powerpieces[Turn_order - 1], Turn_order) #the deployed piece is added to the board state
        
            if type(Board_state) == str: #error check
            
                print(Board_state)
                
        if Deploy_location == 'end' or Deploy_location == 'save': 
            break
        
        #assigning the new board state to the proper variables
        
        Board_pieces = Board_state[0]
        Board_power = Board_state[1]
        Player_powerpieces[Turn_order - 1] = Board_state[2]

        BoardDisp.display(Board_pieces, Board_power, Player_powerpieces) #dusplay the board state when the deploy move is over
    
 
    
    

    ''' MOVE '''
    

    if Turn_choice == 'M':
        
        Board_state = 'initial string'
        
        while type(Board_state) == str: #error chec
            
            print('\nPlayer', Turn_order,', make your move (ex.: \'a3-a4\' will move the piece on A-3 to A-4) (or type \'save\' or \'end\'):') #player inputs their move as coordinates (similar to chess)
            
            Move = input('')
            
            
            '''END OR SAVE'''
            
            if Move == 'end': #when ending the game, the program ends and declares no one is the winner
                winner = 'no one'
                break
            
            if Move == 'save': #when saving the game, the board state is save using the save function                

                BoardDisp.save(Board_pieces, Board_power, Player_powerpieces, Turn_order)                
                winner = 'undecided'
                break
                
            
            Board_state = Movement.movement(Board_pieces, Board_power, Move, Turn_order) #the move is updated on the board state as long as it is valid
        
            if type(Board_state) == str: #error check for the movement
            
                print(Board_state)
    
        if Move == 'end' or Move == 'save':
            break
        
        #assigning the new board state to the proper variables
        
        Board_pieces = Board_state[0]
        Board_power = Board_state[1]
        Player_powerpieces[Turn_order - 1] += Board_state[2]
        
        BoardDisp.display(Board_pieces, Board_power, Player_powerpieces)    
            
    
        
    ''' POWER PIECE '''
        
    Power_piece_location = 'initial string'
    
    if Player_powerpieces[Turn_order - 1] > 0:
            
        while 1>0:
                
            print('\nPlayer', Turn_order,' , do you wish to place a power piece? (Y/n):') #player chooses to put down a power piece or not
                
            confirmation_pp = input('')
                
            if confirmation_pp == 'Y' or confirmation_pp == 'n':
                break
            
            else:
                print('\n Invalid input, try again.')
                
        
        
        
        while type(Power_piece_location) == str: #error check
    
            if confirmation_pp == 'n': #if the player does not want to place a power piece, skip this step
                break
            
            elif confirmation_pp == 'Y':
                
                Power_piece_input = input('Where should it go?:')
            
            Power_piece_location = Movement.powerpiece(Board_pieces, Board_power, Power_piece_input, Player_powerpieces[Turn_order - 1], Turn_order) #the power piece is added to the board state
            
            if type(Power_piece_location) == str: #error check
                
                print(Power_piece_location)
                
                
        if confirmation_pp == 'Y':    
            
            #assigning the new board state to the proper variables
            
            Board_power = Power_piece_location[0]
            Player_powerpieces[Turn_order - 1] = Power_piece_location[1]           
            
            BoardDisp.display(Board_pieces, Board_power, Player_powerpieces)
    
 
    
    '''WINNING CONDITION'''
    
    wincounter = 0
    
    for i in range(Dimension):
        for j in range(Dimension):           
            if Board_pieces[i,j] == Turn_dict[Turn_order] + 2: #counts the number of fortresses (with values of 3 (player 1) and 4 (player 2)) that are on the board
                
                wincounter += 1
                           
    if wincounter < NumFortress: #if any are missing, than the player who removed that fortress wins
        Game_over = True
        winner = Turn_order
 
    
    '''Turn order'''
               
    Turn_order = Turn_dict[Turn_order]
    
print('\n\nThe winner is Player ' + str(winner) + ' !!!' ) #declares the winner