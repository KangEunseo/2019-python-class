from tictactoe import tictactoe
import math
import tkinter

class GameManager:
    def __init__(self):
        self.ttt = tictactoe()

    def play(self):
        #show_board
        print(self.ttt)

        while True: #repeat
            #위치 입력받기
            row = int(input("row: "))
            col = int(input("col: "))

            #말 놓기
            self.ttt.set(row, col)
            print(self.ttt)

            #check_winner()
            if self.ttt.check_winner() == "o":
                print("o 승리!")
                break
            elif self.ttt.check_winner() == "x":
                print("x 승리!")
                break
            elif self.ttt.check_winner() == "d":
                print("무승부")
                break

        #print result
        print(self.ttt)

class GameManager_GUI:
    def __init__(self):
        self.ttt = tictactoe()
        CANVAS_SIZE = 300
        self.TILE_SIZE = CANVAS_SIZE/3

        self.root = tkinter.Tk()
        self.root.title("틱택토")
        self.root.geometry(str(CANVAS_SIZE) + "x" + str(CANVAS_SIZE))
        self.root.resizable(width=False, height=False)

        self.canvas = tkinter.Canvas(self.root, bg="white", width=CANVAS_SIZE, height=CANVAS_SIZE)
        self.canvas.pack()

        self.images = dict()
        self.images["O"] = tkinter.PhotoImage(file="img/O.gif")
        self.images["X"] = tkinter.PhotoImage(file="img/X.gif")

        self.canvas.bind("<Button-1>", self.click_handler)

    def click_handler(self, event):
        row = math.floor(event.y / self.TILE_SIZE)
        col = math.floor(event.x / self.TILE_SIZE)
        self.ttt.set(row, col)
        #self.ttt.check_winner()

    def draw_board(self):
        #clear
        self.canvas.delete("all")

        x = 0
        y = 0

        for i, v in enumerate(self.ttt.board):
            if v == ".":
                pass
            if v == "o":
                self.canvas.create_image(x, y, anchor="nw", image=self.images["O"])
            if v == "x":
                self.canvas.create_image(x, y, anchor="nw", image=self.images["X"])

            x += self.TILE_SIZE
            if i % 3 == 2:
                x = 0
                y += self.TILE_SIZE

    def play(self):
        self.root.mainloop()

if __name__ == '__main__':
    gm = GameManager_GUI()
    gm.ttt.set(1, 1)
    gm.draw_board()
    gm.play()