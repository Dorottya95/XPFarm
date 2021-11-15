Tic Tac Toe Game
Rules: https://en.wikipedia.org/wiki/Tic-tac-toe

GOAL:
The system could be run in BOT mode to print on the screen all player's moves (with a 2 seconds timeout between each round) until someone won or the
game ends with a draw.


Done = 🌞

Guardians:
1. the initial game board should be an empty 3x3 matrix 🌞
2. negative scenario: board is not empty 🌞
3. board should be displayed like this: 🌞
    | |
   -+-+-
    | |
   -+-+-
    | |
4. moves should be handled (e.g. switching between players) 🌞
5. player X won with a vertical line 🌞
6. player O won with a vertical line 🌞
7. player X won with a horizontal line 🌞
8. player O won with a horizontal line 🌞
9. player X won with a diagonal line
10. player O won with a diagonal line
11. game ended with a draw

Steps/Process:
1. create a board 🌞
2. display the board 🌞
3. play the game:
   1. swap between players
   2. remove used spaces 🌞
4. check if there is a winner:
   1. check columns 🌞
   2. check rows 🌞
   3. check diagonals
   4. end the game if there is a winner
5. check draw

DevOps:
