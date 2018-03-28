## TicTacToe player
_A tic-tac-toe player which plays using min max strategy_

### Mini Max strategy
- Every possible position in a tic tac toe game is a frame
- Each frame is mapped to a number(utility) which is proportional to the chance of winning in that frame
- The player chooses the frame with greatest winning probability (max)
- The opponent chooses the frame with least winning probability (min)
- Optimization: apply alpha-beta pruning
