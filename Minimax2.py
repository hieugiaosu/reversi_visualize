import numpy as np
import random as rd
player = np.array([
        [150, -50, 10, 5, 5, 10, -50, 150],
        [-50, -100, -1, -1, -1, -1, -100, -50],
        [10, -1, 3, 2, 2, 3, -1, 10],
        [5, -1, 2, 1, 1, 2, -1, 5],
        [5, -1, 2, 1, 1, 2, -1, 5],
        [10, -1, 3, 2, 2, 3, -1, 10],
        [-50, -100, -1, -1, -1, -1, -100, -50],
        [150, -50, 10, 5, 5, 10, -50, 150]
    ])


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
def winner(board):
    count = np.sum(board)
    if count>0: return 1
    if count<0: return -1
    return 0
def heuristic(board,player_to_move):
    state = np.array(board)
    return (np.sum(player[state==player_to_move]) - np.sum(player[state==-player_to_move])) 

def first_maximize(board,player_to_move,depth,valid_moves,min1=-np.Inf, min2=-np.Inf):
    max_reward = -np.Inf
    move = valid_moves[0]
    for i in valid_moves:
        if min1 > -min2: break
        reward = -maximize_reward(make_move(board,i[0],i[1],player_to_move),-1*player_to_move,depth-1,min1,min2)
        if reward > max_reward:
            max_reward = reward
            move = i
        if player_to_move == 1: min1 = max(reward,min1)
        else: min2 = max(reward,min2)
    return move

def maximize_reward(board,player_to_move,depth,min1=-np.Inf, min2=-np.Inf):
    if depth == 0:
        return heuristic(board,player_to_move)
    valid_moves = get_valid_moves(board,player_to_move)
    if valid_moves == [] and get_valid_moves(board,player_to_move*-1) == []:
        if winner(board) == 0: return 0
        if winner(board) == player_to_move: return np.Inf
        else: return -1*np.Inf
    if valid_moves == []:
        return -maximize_reward(board,player_to_move*-1,depth-1,min1,min2)
    max_reward = -np.Inf
    for i in valid_moves:
        if min1 > -min2: break
        reward = -maximize_reward(make_move(board,i[0],i[1],player_to_move),-1*player_to_move,depth-1,min1,min2)
        if reward > max_reward: max_reward = reward
        if player_to_move == 1: min1 = max(reward,min1)
        else: min2 = max(reward,min2)
    return max_reward

def select_move(cur_state, player_to_move, remain_time):
    valid_moves = get_valid_moves(cur_state, player_to_move)
    if valid_moves == []: return None
    if len(valid_moves)==1: return valid_moves[0]
    if np.count_nonzero(cur_state) > 48: return first_maximize(cur_state,player_to_move,7,valid_moves)
    if np.count_nonzero(cur_state) > 53: return first_maximize(cur_state,player_to_move,10,valid_moves)
    return first_maximize(cur_state,player_to_move,5,valid_moves)

