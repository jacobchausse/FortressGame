from datetime import datetime
import numpy as np
import os

'''
print('     1     2     3     4     5     6     7   ')
print('  ,-----,-----,-----,-----,-----,-----,-----,')
print('A |[[1]]| [1] |     |     |     | {1} |{{1}}|')
print('  |-----|-----|-----|-----|-----|-----|-----|')
print('B | [1] | [1] |     |     |     | {1} | {1} |')
print('  |-----|-----|-----|-----|-----|-----|-----|')
print('C | [1] | [1] |     |     |     | {1} | {1} |')
print('  |-----|-----|-----|-----|-----|-----|-----|')
print('D |[[1]]| [1] |     |     |     | {1} |{{1}}|')
print('  |-----|-----|-----|-----|-----|-----|-----|')
print('E | [1] | [1] |     |     |     | {1} | {1} |')
print('  |-----|-----|-----|-----|-----|-----|-----|')
print('F | [1] | [1] |     |     |     | {1} | {1} |')
print('  |-----|-----|-----|-----|-----|-----|-----|')
print('G |[[1]]| [1] |     |     |     | {1} |{{1}}|')
print('  \'-----\'-----\'-----\'-----\'-----\'-----\'-----\'')
print('\n  > P1: [0]        POWER PIECES      > P2: {0}')

'''


Dimension = 7


Spacer = '    |-----|-----|-----|-----|-----|-----|-----|'

Starter = '       1     2     3     4     5     6     7   \n    ,-----,-----,-----,-----,-----,-----,-----,'

Ender = '    \'-----\'-----\'-----\'-----\'-----\'-----\'-----\''


def display(Board_pieces, Board_power, Power_pieces):
    '''
    Displays (prints) the board as terminal text where:
        -Board_pieces is the 7x7 array of the board state (1 = player1 piece, 2 = player2 piece, 3 = player1 fortress, 4 = player2 fortress 0 = no piece)
        -Board_power is the 7x7 array of the power of each piece on the board where the number corresponds to the power and 0 where there are no pieces
        -Power_pieces is the length 2 list of the number of power pieces each player has (entry 0 contains the info for player 1 and entry 1 has info for player 2)
    Returns: None (simply prints the text on screen)
    '''
    
    
    print(Starter)
    
    boardstrlist = ['  A |','  B |','  C |','  D |','  E |','  F |','  G |'] #length of list depends on the dimension
    
    for i in range(Dimension):
        
        for j in range(Dimension):
            
            if Board_pieces[i,j] != 0:
                
                if Board_pieces[i,j] == 1:
                    
                    boardstrlist[i] += ' [' + str(Board_power[i,j]) + '] |' 
                
                elif Board_pieces[i,j] == 2:
                    
                    boardstrlist[i] += ' {' + str(Board_power[i,j]) + '} |'
        
                elif Board_pieces[i,j] == 3:
                    
                    boardstrlist[i] += '[[' + str(Board_power[i,j]) + ']]|' 
                
                elif Board_pieces[i,j] == 4:
                    
                    boardstrlist[i] += '{{' + str(Board_power[i,j]) + '}}|'
            
            elif Board_pieces[i,j] == 0:
            
                boardstrlist[i] += '     |'
            
    
    for k in range(Dimension - 1):
        
        print(boardstrlist[k])
        print(Spacer)
    
    print(boardstrlist[-1])
    
    print(Ender)
    
    print('\n    > P1: [' + str(Power_pieces[0]) + ']     - POWER PIECES -    > P2: {' + str(Power_pieces[1]) + '}')
    
    
    
    return(None)
            

def save(Board_pieces, Board_power, Power_pieces, Player_turn):
    
    date = datetime.now()
    date_time = os.path.dirname(os.path.abspath(__file__)) + '\\saves\\fortressSAVE_' + date.strftime("%m.%d.%Y_%H.%M.%S")
    
    filedata = np.array([Board_pieces, Board_power, Power_pieces, Player_turn], dtype=object)
    
    np.savez(date_time, filedata)
    
    
def load():

    saves = os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\saves\\')
    
    if len(saves) == 0:
        return(False)
      
    print('\nAvailable saves:')
    
    for n in range(len(saves)):
        print('\n' + str(n+1) + '. ' + saves[n])
           
    saveChoice = input('\nChoose save (type corresponding number):')
    
    if (not saveChoice.isdigit()):
            return('\nInput is not an integer.\n')
            
    elif not(int(saveChoice) <= len(saves) and int(saveChoice) > 0):
            return('\nInput is not in the list of saves.\n')
  
    return(np.load(os.path.dirname(os.path.abspath(__file__)) + '\\saves\\' + saves[int(saveChoice)-1], allow_pickle=True))
