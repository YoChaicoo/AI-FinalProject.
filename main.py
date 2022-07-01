import tkinter as tk
from board_gui import BoardFrame

import os
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0')


def main():
    # window = tk.Tk()
    # window.wm_title("GOMOKU GAME")
    # gui_board = BoardFrame(window)
    # gui_board.pack()
    # window.mainloop()

    board_frame = BoardFrame()




if __name__ == "__main__":
    main()
