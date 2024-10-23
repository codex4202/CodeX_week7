import random

def Sarah_initialize_board():
    return [' ' for Sarah_i in range(9)]

def Sarah_print_board(Sarah_board):
    for Sarah_i in range(0, 9, 3):
        print(Sarah_board[Sarah_i:Sarah_i+3])

def Sarah_check_winner(Sarah_board):
    Sarah_win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for Sarah_wc in Sarah_win_conditions:
        if Sarah_board[Sarah_wc[0]] == Sarah_board[Sarah_wc[1]] == Sarah_board[Sarah_wc[2]] != ' ':
            return Sarah_board[Sarah_wc[0]]
    if ' ' not in Sarah_board:
        return 'Sarah_Draw'
    return None

class Sarah_MENACE:
    def _init_(self):
        self.Sarah_matchboxes = {}

    def Sarah_get_board_key(self, Sarah_board):
        return ''.join(Sarah_board)

    def Sarah_select_move(self, Sarah_board):
        Sarah_board_key = self.Sarah_get_board_key(Sarah_board)
        if Sarah_board_key not in self.Sarah_matchboxes:
            self.Sarah_matchboxes[Sarah_board_key] = [1 if Sarah_board[Sarah_i] == ' ' else 0 for Sarah_i in range(9)]
        Sarah_moves = self.Sarah_matchboxes[Sarah_board_key]
        Sarah_total_beads = sum(Sarah_moves)
        if Sarah_total_beads == 0:
            return None
        Sarah_move = random.choices(range(9), weights=Sarah_moves)[0]
        return Sarah_move

    def Sarah_update_matchbox(self, Sarah_board, Sarah_move, Sarah_result):
        Sarah_board_key = self.Sarah_get_board_key(Sarah_board)
        if Sarah_result == 'Sarah_win':
            self.Sarah_matchboxes[Sarah_board_key][Sarah_move] += 3
        elif Sarah_result == 'Sarah_lose':
            self.Sarah_matchboxes[Sarah_board_key][Sarah_move] = max(1, self.Sarah_matchboxes[Sarah_board_key][Sarah_move] - 1)
        elif Sarah_result == 'Sarah_draw':
            self.Sarah_matchboxes[Sarah_board_key][Sarah_move] += 1

def Sarah_play_game(Sarah_menace):
    Sarah_board = Sarah_initialize_board()
    Sarah_player_turn = random.choice(['Sarah_MENACE', 'Sarah_Human'])
    Sarah_history = []

    while True:
        Sarah_print_board(Sarah_board)
        Sarah_winner = Sarah_check_winner(Sarah_board)
        if Sarah_winner:
            print(f"Sarah_Game Over! Sarah_Winner: {Sarah_winner}")
            return Sarah_winner, Sarah_history

        if Sarah_player_turn == 'Sarah_MENACE':
            Sarah_move = Sarah_menace.Sarah_select_move(Sarah_board)
            if Sarah_move is None:
                return 'Sarah_Draw', Sarah_history
            Sarah_board[Sarah_move] = 'X'
            Sarah_history.append((Sarah_board.copy(), Sarah_move))
            Sarah_player_turn = 'Sarah_Human'
        else:
            Sarah_move = int(input("Enter your Sarah_move (0-8): "))
            if Sarah_board[Sarah_move] == ' ':
                Sarah_board[Sarah_move] = 'O'
                Sarah_player_turn = 'Sarah_MENACE'

def Sarah_train_menace(Sarah_games):
    Sarah_menace = Sarah_MENACE()
    for Sarah_game in range(Sarah_games):
        print(f"\nStarting Sarah_Game {Sarah_game + 1}")
        Sarah_winner, Sarah_history = Sarah_play_game(Sarah_menace)
        
        if Sarah_winner == 'X':
            Sarah_result = 'Sarah_win'
        elif Sarah_winner == 'O':
            Sarah_result = 'Sarah_lose'
        else:
            Sarah_result = 'Sarah_draw'

        for Sarah_board, Sarah_move in Sarah_history:
            Sarah_menace.Sarah_update_matchbox(Sarah_board, Sarah_move, Sarah_result)

    print("\nSarah_Training has been completed. Sarah_MENACE is now ready to play!") 

if _name_ == "_main_":
    Sarah_train_menace(10)
