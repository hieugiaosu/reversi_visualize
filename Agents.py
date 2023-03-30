
import random as rd

def random_agent(cur_state, player_to_move, remain_time):
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
    valid_moves = get_valid_moves(cur_state,player_to_move)
    if valid_moves == []: return None
    else: return rd.choice(valid_moves)
def move_by_yourself(cur_state, player_to_move, remain_time):
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
    valid_moves = get_valid_moves(cur_state,player_to_move)
    if valid_moves == []: return None
    print(valid_moves)
    a = int(input())
    return valid_moves[a]