#!/usr/bin/env python3

class BingoBoard(object)
    def __init__(self, board: List[List[int]]):
        # Each square is a dict that contains 'val' and 'marked' keys
        # 'val' => actual value, 'marked' => True if marked
        self.board = []

        # Hash table that maps values on board to their locations on board.
        # Locations stored as list of tuples containing row, column index
        self.val_to_loc_map = {}

        self.has_won = False
        self.final_score = 0
        self.most_recently_marked_val = 0

        for board_row in board:
            new_board_row = []
            for val in board_row:
                new_board_row.append({ 'val': val, 'marked': False })
            self.board.append(new_board_row)

        for row_i, board_row in enumerate(self.board):
            for col_i, square in enumerate(board_row):
                if square['val'] in self.val_to_loc_map:
                    self.val_to_loc_map[square['val']].append((row_i, col_i))
                else:
                    self.val_to_loc_map[square['val']] = list((row_i, col_i))

    def has_won(self):
        return self.has_won

    def check_row_for_win(self, row_i):
        is_row_a_winner = True

        for square in self.board[row_i]:
            if not square['marked']:
                is_row_a_winner = False
                break

        if is_row_a_winner:
            self.has_won = True

    def check_col_for_win(self, col_i):
        is_col_a_winner = True

        for row_i in xrange(len(self.board)):
            square = self.board[row_i][col_i]
            if not square['marked']:
                is_col_a_winner = False
                break

        if is_col_a_winner:
            self.has_won = True

    def has_val(self, val):
        return val in self.val_to_loc_map

    def mark_val(self, val):
        if val in self.val_to_loc_map:
            for loc in self.val_to_loc_map[val]:
                row_i, col_i = loc
                self.board[row_i][col_i]['marked'] = True
                self.check_row_for_win(row_i)
                self.check_col_for_win(col_i)
                self.most_recently_marked_val = val

        return True

    def calc_final_score(self):
        sum_unmarked = 0

        for row in self.board:
            for square in row:
                if not square['marked']:
                    sum_unmarked += square['val']

        self.final_score = sum_unmarked * self.most_recently_marked_val
        return self.final_score

