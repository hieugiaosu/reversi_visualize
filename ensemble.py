import numpy as np
import random as rd
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import load
import Minimax2 as mn
count =0
miss_count =0
INITIAL_STATE = [[0,0,0,0,0,0,0,0], 
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,1,-1,0,0,0],
                 [0,0,0,-1,1,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0]]
dt = load('training/ensemble.joblib')
def is_valid_move(board, row, col, turn):
    if board[row][col] != 0:
        return False
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            r = row + i 
            c = col + j
            found_opponent = False
            while r >= 0 and r < 8 and c >= 0 and c < 8:
                if board[r][c] == 0:
                    break
                if board[r][c] == turn:
                    if found_opponent:
                        return True
                    break
                found_opponent = True
                r += i
                c += j
    return False
def get_valid_moves(board, turn):
    valid_moves = []
    for row in range(8):
        for col in range(8):
            if is_valid_move(board, row, col, turn):
                valid_moves.append((row, col))
    return valid_moves
def make_move(board, row, col, turn):
    new_board = [row[:] for row in board]
    new_board[row][col] = turn
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue 
            r = row + i
            c = col + j
            flipped = False
            to_flip = []
            while r >= 0 and r < 8 and c >= 0 and c < 8:
                if new_board[r][c] == 0:
                    break
                if new_board[r][c] == turn:
                    flipped = True
                    break
                to_flip.append((r, c))
                r += i
                c += j
            if flipped:
                for (r, c) in to_flip:
                    new_board[r][c] = turn    
    return new_board
def select_move(cur_state, player_to_move, remain_time):
    global miss_count
    global count
    valid_moves = get_valid_moves(cur_state,player_to_move)
    if valid_moves == []: return None
    count+=1
    move_tensor = np.zeros(65,dtype=int)
    for i in valid_moves:
        move_tensor[i[0]*8+i[1]]=1
    state_tensor = np.array(cur_state)
    state_tensor = np.reshape(state_tensor,(64,))
    state_tensor = np.append(state_tensor,player_to_move)
    state_tensor = np.append(state_tensor,move_tensor)
    state_tensor = np.reshape(state_tensor,(-1,130))
    move = int(dt.predict(state_tensor)[0])
    if int(move_tensor[move]) == 0:
        miss_count +=1 
        return mn.select_move(cur_state,player_to_move,remain_time)
    return (move//8, move%8)



















