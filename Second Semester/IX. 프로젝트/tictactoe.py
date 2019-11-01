class tictactoe:
    def __init__(self):
        self.board = [".", ".", ".", ".", ".", ".", ".", ".", "."]
        self.current_turn = "o"

    def set(self, row, col):
        if self.get(row, col) == ".":
            # if self.current_turn == "o":
            #     self.current_turn = "x"
            # else:
            #     self.current_turn = "o"
            self.current_turn = "o" if self.current_turn == "x" else "x"
            self.board[(row * 3) + col] = self.current_turn

    def get(self, row, col):
        return self.board((row * 3) + col)

    def check_winner(self):
        check = self.current_turn
        for i in range(3):
            if self.get(i, 0) == self.get(i, 1) == self.get(i, 2) == check:
                return check
            if self.get(0, i) == self.get(1, i) == self.get(2, i) == check:
                return check

        if self.get(0, 1) == self.get(1, 1) == self.get(2, 1) == check:
            return check
        if self.get(0, 2) == self.get(1, 2) == self.get(2, 2) == check:
            return check

        if not "," in self.board:
            return "d"

    def __str__(self):
        s = ""
        for i, ch in enumerate(self.board):
            s += ch
            if i % 3 == 2:
                s += "\n"
        return s

if __name__ == '__main__':
    ttt = tictactoe()
    print(ttt)
    ttt.set(1, 1)
    ttt.set(1, 2)
    ttt.set(1, 3)
    ttt.set(2, 1)
    ttt.set(2, 2)
    ttt.set(0, 2)
    print(ttt)