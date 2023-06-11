Hello this is Shivansh Bhatnagar(Roll no. 22124042) of Mathematics and Computing (IDD)
This is my very first project created using python GUI library
To view this project in its best form:
1)	Make sure you have customtkinter installed in your device
	1a)	To install customtkinter just type "pip install customtkinter" in the terminal
2)	Please install the font Atarian provided with this project for best graphics

This is the game of minesweeper

Minesweeper is a classic computer game that involves clearing a minefield without detonating any mines. The rules of Minesweeper are relatively simple:

Objective: The goal of the game is to uncover all the empty squares on the minefield without triggering any mines. You win the game by clearing all the non-mine squares.
Game Grid: The minefield is represented by a grid of squares. Each square can be in one of three states: uncovered, covered, or flagged.
Mines: Randomly placed mines are hidden throughout the minefield. The number of mines is predetermined based on the difficulty level you choose at the beginning of the game.
Numbers: Each uncovered square, except for those containing a mine, will display a number. The number indicates how many mines are present in the adjacent squares—diagonally and horizontally.
Uncovering Squares: You can uncover a square by left-clicking on it. If you uncover a square containing a mine, you lose the game. However, if you uncover a square without a mine, it will display a number indicating the number of mines in its vicinity. If there are no mines nearby, it will automatically uncover neighboring squares.
Flagging Mines: If you suspect a square contains a mine, you can flag it by right-clicking on it. This allows you to mark potential mine locations without triggering them. Flagging can be useful for keeping track of potential mine locations.
Adjacent Squares: When a square is uncovered, its neighboring squares will be automatically uncovered if they do not contain any mines. This process continues recursively until all adjacent squares are cleared, creating a chain reaction.
Winning and Losing: You win the game by uncovering all non-mine squares. If you uncover a mine, the game ends, and you lose. Additionally, some versions of the game include a timer, so you can try to beat your previous time records.