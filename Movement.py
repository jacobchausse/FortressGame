
import numpy as np


Position_legend = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7} 

Dimension = 6 #remember to subtract 1 and update the Position_legend when changing


def movement(Board_pieces, Board_power, Move_input, Player_turn):
    
    '''
    Moves pieces and completes battles according to the input of the player where:
        -Board_pieces is the 7x7 array of the board state (1 = player1 piece, 2 = player2 piece, 3 = player1 fortress, 4 = player2 fortress 0 = no piece)
        -Board_power is the 7x7 array of the power of each piece on the board where the number corresponds to the power and 0 where there are no pieces
        -Move_input is the string that indicates the origin and target position of the piece (format of 'a1-b2')
        -Player_turn is the int that indicates which player's turn it is, 1 if player1 and 2 if player2
        
        Returns: string of error code OR updated info in a tuple: (Board_pieces, Board_power, Power_pieces)
    '''


    if len(Move_input) != 5 or (not Move_input[0] in Position_legend) or (not Move_input[3] in Position_legend) or Move_input[2] != '-' or not Move_input[1].isnumeric() or not Move_input[4].isnumeric():
        
        return('\n Wrong Formating (use format: a1-b2)')
        
        
        
    Origin = (Position_legend[Move_input[0]]-1, int(Move_input[1])-1)
    
    Target = (Position_legend[Move_input[3]]-1, int(Move_input[4])-1)    
        
    
    AllowedMovement = Board_power[Origin[0], Origin[1]]
    
    if Origin == Target:
        
        return('\n Wrong Coordinate (Target cannot be the same as Origin)')
        
    elif Board_pieces[Origin] == 3 or Board_pieces[Origin] == 4:

        return('\n Wrong Origin (Chosen piece must not be a Fortress!)')
    
    elif Board_pieces[Origin] != Player_turn:
        
        return('\n Wrong Origin (Chosen piece must be Friendly!)') 
    
    elif abs(Origin[0] - Target[0]) > AllowedMovement or abs(Origin[1] - Target[1]) > AllowedMovement:
        
        return('\n Wrong Coordinate (Must move by only ' + str(AllowedMovement) + ' tile in any direction!)')
    
    elif Origin[0] > Dimension or Origin[1] > Dimension or Target[0] > Dimension or Target[1] > Dimension or Origin[0] < 0 or Origin[1] < 0 or Target[0] < 0 or Target[1] < 0: 
        
        return('\n Wrong Coordinate (Out of bounds!)')
    
    elif Board_pieces[Target] == Player_turn or Board_pieces[Target] == Player_turn + 2:
        
        return('\n Wrong Target (Friendly piece is targeted!)')
        

  
    
    """SAMPLE CODE (STARTS)"""
    
    #This code is used in a chess-type game where pieces can move in any horizontal, vertical or diagonal direction. This sample is used to check if the player attempts to move a piece in any other direction or if there is a different piece blocking the path. 
    #The Target and Origin variables are simply tuples containing the coordinates of the piece (Origin) and where the player wants to move it (Target). They therefore have 2 elements.
    #The Board_pieces variable is a 7x7 matrix representing the board. It contains 0 if there is no piece there, 1 if there is a player1 piece and 2 if there is a player2 piece.
    

    if AllowedMovement > 1:
        
        if Origin[1]-Target[1] != 0: #to avoid infinite slopes
            
            Slope = (Origin[0]-Target[0])/(Origin[1]-Target[1]) #calculate the slope of the target versus origin
        
            if Slope != 1 and Slope != 0 and Slope != -1: #if the slope is not horizontal or in the diagonals
            
                return('Wrong Target (Must be in a horizontal, vertical or diagonal line)') #return error message because pieces should only move in a diagonal, vertical or horizontal direction
    
        
        
        spaces = abs((Origin[1] - Target[1])*(abs(Origin[0] - Target[0]) == 0) + (Origin[0] - Target[0])*(abs(Origin[0] - Target[0]) != 0)) #calculates the number of spaces between the origin and target
        
        line = np.linspace(Origin, Target, spaces+1)[1:-1,:] #creates a vector of coordinates of all spaces between the origin and target
        
        for i in range(line.shape[0]): #to check all coordinate pairs
            
            Linei = line[i,:] #isolates a single pair of coordinates   
            
            Locationi = tuple(int(s) for s in Linei) #makes the array into a tuple for indexing
             
            if Board_pieces[Locationi] != 0: #if there is a piece found at the coordinate
                    
                return('Wrong Target (There is an occupied space between the Origin and the Target)') #return the error message
        
        
    
    """SAMPLE CODE (END)"""
    
    
    
    
    if Board_pieces[Target] == 0: #case where the target tile is empty
        
        Board_pieces[Target] = Player_turn
        Board_pieces[Origin] = 0
        
        Board_power[Target] = Board_power[Origin]
        Board_power[Origin] = 0
        
        return(Board_pieces, Board_power, 0)
    

    
    else: #case where there is a battle
        
        Power_pieces = 0
        
            
        if Board_power[Origin] == Board_power[Target]:
            
            Board_pieces[Target] = Player_turn
            Board_pieces[Origin] = 0
    
            Board_power[Target] = 1
            Board_power[Origin] = 0
                
            Power_pieces = 1
                
        elif Board_power[Origin] > Board_power[Target]:
                
            Board_pieces[Target] = Player_turn
            Board_pieces[Origin] = 0
    
            Board_power[Target] = Board_power[Origin] - Board_power[Target]
            Board_power[Origin] = 0

            Power_pieces = 2
                

        elif Board_power[Origin] < Board_power[Target]:
                
            Board_pieces[Origin] = 0
        
            Board_power[Target] = Board_power[Target] - Board_power[Origin]
            Board_power[Origin] = 0 
            
        return(Board_pieces, Board_power, Power_pieces)                     
        

        
                
                
                
def powerpiece(Board_pieces, Board_power, Power_piece_input, Power_pieces, Player_turn): 
    
    '''
    Assigns power pieces to the proper pieces on the board where:
        -Board_pieces is the 7x7 array of the board state (1 = player1 piece, 2 = player2 piece, 3 = player1 fortress, 4 = player2 fortress 0 = no piece)
        -Board_power is the 7x7 array of the power of each piece on the board where the number corresponds to the power and 0 where there are no pieces
        -Power_piece_input is the location of the piece to be placed (format of 'a2')
        -Power_pieces is the number of power pieces associated with the player who's turn it is
        -Player_turn is the int that indicates which player's turn it is, 1 if player1 and 2 if player2
        
        
        Returns: string of error code OR updated info in a tuple: (Board_power, Power_pieces)
    '''         


    if len(Power_piece_input) != 2 or (not Power_piece_input[0] in Position_legend) or not Power_piece_input[1].isnumeric():
        
        return('\n Wrong Formating (use format: a1)')
        
        
        
    Target = (Position_legend[Power_piece_input[0]]-1, int(Power_piece_input[1])-1)    
    

    if Board_pieces[Target] == 0:
        
        return('\n Wrong Target (There must be a piece at the location!)')
    
    elif Board_pieces[Target] != Player_turn and Board_pieces[Target] != Player_turn + 2:
        
        return('\n Wrong Target (Enemy piece is targeted!)')
    
    elif Board_power[Target] == 4:
        
        return('\n Wrong Target (The piece already has maximum power (4)!)')
    
    
    
    if Board_pieces[Target] == Player_turn:
    
        Board_power[Target] += 1
        
        Power_pieces -= 1
    
    elif Board_pieces[Target] == Player_turn + 2 and Power_pieces >= 2:
        
        Board_power[Target] += 1
        
        Power_pieces -= 2
        
    elif Board_pieces[Target] == Player_turn + 2 and Power_pieces < 2:
        
        return('\n You do not have enough power pieces to upgrade this fortress!')
        
    
    return(Board_power, Power_pieces)
        
   


     

def deploy(Board_pieces, Board_power, Deploy_location, Power_pieces, Player_turn):

    '''
    Deploys power pieces as normal pieces on the board where:
        -Board_pieces is the 7x7 array of the board state (1 = player1 piece, 2 = player2 piece, 3 = player1 fortress, 4 = player2 fortress 0 = no piece)
        -Board_power is the 7x7 array of the power of each piece on the board where the number corresponds to the power and 0 where there are no pieces
        -Deploy_location is the deploy location (format of 'a2')
        -Power_pieces is the number of power pieces associated with the player who's turn it is
        -Player_turn is the int that indicates which player's turn it is, 1 if player1 and 2 if player2
        
        
        Returns: string of error code OR updated info in a tuple: (Board_pieces, Board_power, Power_pieces)
    ''' 
    
    
    if len(Deploy_location) != 2 or (not Deploy_location[0] in Position_legend) or not Deploy_location[1].isnumeric():
        
        return('\n Wrong Formating (use format: a1)')
        
        
    Target = (Position_legend[Deploy_location[0]]-1, int(Deploy_location[1])-1)    
    


    if Board_pieces[Target] != 0:
        
        return('\n Wrong Target (The deploy zone must be vacant!)')
    
    
    Adjacent_fortress = False
    
    Adjacent_tiles = []
    
    for i in range(3):
        
        number1 = i - 1
        
        for j in range(3):
            
            number2 = j - 1
            
            if 0 <= Target[0] + number1 <= Dimension and 0 <= Target[1] + number2 <= Dimension:
                
                Adjacent_tiles.append((Target[0] + number1, Target[1] + number2))
                
    
    for i in range(len(Adjacent_tiles)):
        
        if Board_pieces[Adjacent_tiles[i]] == Player_turn + 2:
        
            Adjacent_fortress = True
            
            break
    
    if Adjacent_fortress == False:
        
        return('\n Wrong Target, the deploy zone must be adjacent to a friendly fortress!')
    
    
    Board_pieces[Target] = Player_turn
    Board_power[Target] = 1
    
    
    return(Board_pieces, Board_power, Power_pieces - 1)
        
        
        
    
    
    
def deploy_check(Board_pieces, Player_turn):
    
    '''
    Checks if there is an available slot for deployment around friendly fortresses where:
        -Board_pieces is the 7x7 array of the board state (1 = player1 piece, 2 = player2 piece, 3 = player1 fortress, 4 = player2 fortress 0 = no piece)
        -Player_turn is the int that indicates which player's turn it is, 1 if player1 and 2 if player2
        
        Returns: True if slot is available or False otherwise
    '''
    
    
    list_f = []
    
    for i in range(Board_pieces.shape[0]):
        
        for j in range(Board_pieces.shape[1]):
            
            if  Board_pieces[i,j] == Player_turn + 2:
                
                list_f.append((i,j))
                                                                                                                        
    deployslot = False
    
    for h in range(len(list_f)):
        
        for k in range(3):
        
            number1 = k - 1
        
            for l in range(3):
            
                number2 = l - 1
                
                if 0 <= list_f[h][0] + number1 <= Dimension and 0 <= list_f[h][1] + number2 <= Dimension:
                    
                    if Board_pieces[list_f[h][0] + number1, list_f[h][1] + number2] == 0:
                        
                        deployslot = True
                        
                        break
            
            if deployslot == True:
                
                break
            
        if deployslot == True:
                
            break  
        
    return(deployslot)                      
                        

    
    
    
    