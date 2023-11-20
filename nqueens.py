from typing import *

def nQueensAllSolutions(n: int) -> Tuple[List[int], List[List[str]]]:
    
    # columns consumed in a particular Queen-place cycle
    col = set()

    # +ve and -ve diagonal
    pos_diag = set()
    neg_diag = set()

    # constructing the chess board
    chess_board = [["."]*n for _ in range(n)]

    # result list, copy of an accomplished state is appended when encountered everytime
    moves = list()
    solution_moves = list()
    
    def backTrack(r: int = 0) -> None:
        # r -> row count of the board

        # base-case -> when r count comes to n, all rows have been assigned 
        # with a queen hence a valid sol is encountered
        if r == n:
            # make a copy of artboard
            copy = [row.copy() for row in chess_board]
            solution_moves.append(moves.index(copy))
            return
        
        # else, apply queen to possible cols if they meet constraints and recurse to the next row
        for c in range(n):
            # all columns from 0 -> n-1 is considered
            # if the current column doesn't meet constraints below then skip the columns and go check next
            if c in  col or (r+c) in pos_diag or (r-c) in neg_diag:
                continue # skipping the action of placing queen in current row

            # else, if queen can be placed
            chess_board[r][c] = "Q"
            
            col.add(c)
            pos_diag.add(r+c)
            neg_diag.add(r-c)

            # adding the copy of current move to moves list
            moves.append([i.copy() for i in chess_board])

            # go for the next row
            backTrack(r+1)

            # cleanup process... after backtracking to the current row to try next column

            chess_board[r][c] = "."
            col.discard(c)
            pos_diag.discard(r+c)
            neg_diag.discard(r-c)

    # calling the backtracking function
    backTrack()
    
    return solution_moves, moves 


if __name__ == "__main__":
    # print(*nQueensAllSolutions(4), sep="\n")
    sol_list, solutions = nQueensAllSolutions(4)
    for cnt, solution in enumerate(solutions):
            # replacing "." with "⬜️" and "Q" with "🟧"
            # st.header(("😃✅ Valid Solution - Move Count {}"
            #             if cnt in sol_list else
            #             "🤔🥱 Haven't reached the solution yet - Move Count {}")
            #             .format(cnt+1))

            holder = list()
            for k in solutions:
                for i in k:
                    inter = list()
                    for j in i:
                        if j == ".":
                            inter.append("⬜️")
                        else:
                            inter.append("🟧")
                    holder.append(inter)
            # holder = [[("⬜️" if so=="." else "🟧") for so in sol] for sol in solutions]
            print(holder)