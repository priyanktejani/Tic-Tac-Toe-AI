import tictactoe as tx

EMPTY = None
X = "X"
O = "O"
 
x = [[O, X, X],
    [O, O, X],
    [EMPTY, O, EMPTY]]

        

# print(tx.player(x))
# print(tx.actions(x))
# print(tx.result(x, (1, 2)))
# print(tx.terminal(x))
# print(tx.utility(x))
print(tx.minimax(x))
