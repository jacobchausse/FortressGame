
import numpy as np

def around_check(Board_pieces, Origin, Target, AllowedMovement, Dimension):
    
    '''
    Checks if there are empty spaces in a straight line around the piece:
        -Board_pieces is the 7x7 array of the board state (1 = player1 piece, 2 = player2 piece, 3 = player1 fortress, 4 = player2 fortress 0 = no piece)
        -Player_turn is the int that indicates which player's turn it is, 1 if player1 and 2 if player2
        -AllowedMovement is the power of the target piece
        
        Returns: True if there is at least 1 empty space or False otherwise
    '''
    
    if Origin[1]-Target[1] != 0:
        
        Slope = (Origin[0]-Target[0])/(Origin[1]-Target[1])
    
        if Slope != 1 or Slope != 0 or Slope != -1:
        
            isGap = 'Wrong Target (Must be in a horizontal, vertical or diagonal line)'
        
    else:
        
        y = np.array(range(Origin[0]+1,Target[0]))[np.newaxis]
        x = np.array(range(Origin[1]+1,Target[1]))[np.newaxis]
        
        Line = np.concatenate((x,y),1)
        
        for i in range(Line.shape[0]):
            
            if Board_pieces[tuple(Line[i,:])] != 0:
                
                isGap = 'Wrong Target (There is an occupied space between the Origin and the Target)'     
            
    
    return(isGap)                      
                        
