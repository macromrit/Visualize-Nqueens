import streamlit as st
import pandas as pd
import time

# importing nqueens module
import nqueens

container = st.container()

# number_of_queens = st.slider(label="Choose the count of queens to be placed", min_value=3, max_value=10)

code = """
def nQueensAllSolutions(n):
    col = set() # to keep track on columns reserved
    pos_diag = set() # to keep track on +ve diagonals reserved
    neg_diag = set() # to keep track on -ve diagonals reserved

    # to store valid solutions
    res = list() # or []

    # chess-board --> "." - empty block \ "Q" - Queen's in the block
    chess_board = [["."]*n for _ in range(n)]

    def backTrack(r: int = 0):

        # base-case -> when you fill all rows then a valid state
        if r == n:
            # take a copy
            cp = ["".join(i) for i in chess_board]
            return res.append(cp)
        
        # else
        # get all possible indices of columns
        for c in range(n):
            # checking whether the contraints are satisfied or not
            if c in col or (r-c) in neg_diag or (r+c) in pos_diag:
                continue

            # if those are satisfied 
            chess_board[r][c] = "Q"
            col.add(c)
            pos_diag.add(r+c)
            neg_diag.add(r-c)

            backTrack(r+1)

            # clean-up procedure... comming back from a future state
            chess_board[r][c] = "."
            col.remove(c)
            pos_diag.remove(r+c)
            neg_diag.remove(r-c)
    
    # calling the backTracking function
    backTrack()

    return res
"""

# st.title("Table Example")

# # Create the table
# st.dataframe(data=pd.DataFrame([[100] * 13 for i in range(13)]), height=400)


with container:
    col1, col2, _ = st.columns([1,15,1])

    # Place your table or element in the second column
    with col2:
        # Create an expander that contains the table
        # with st.expander("Table", expanded=True):

        st.markdown("# Its N-Queens today 😄👑")

        st.write("""
<br>
""", unsafe_allow_html=True)

        st.markdown("""##### Hey its Amrit Subramanian.C
##### Do check out my <a href='https://github.com//macromrit'>github</a> and <a href='https://www.linkedin.com/in/macromrit/'>linked-in</a>""", unsafe_allow_html=True)
        
        st.write("""
<br>
""", unsafe_allow_html=True)

        st.markdown("""
#### PS Explanation 🙊 :
###### N is an integer input given by user
###### Based on that, we have to place N queens in an NxN chess board
###### Such that, No Queens threaten each other (Diagonally, Column wise and Row wise)
""")
        
        st.write("""
<br><br>
""", unsafe_allow_html=True)

        number_of_queens = st.slider(label="Choose the count of queens to be placed (N)", min_value=4, max_value=10)

        st.write("""
<br><br>
""", unsafe_allow_html=True)
        
        st.markdown("### Get to know on the Go 🔑")
        st.markdown("##### ⬜️ this is an empty block on the chess board")
        st.markdown("##### 🟧 this is a block holding a queen on the chess board")

        st.write("""
<br><br>
""", unsafe_allow_html=True)
        
        with st.expander("Solution formulated in Python 🐍", expanded=True):
            
            st.code(code, language='python')

        st.write("""
<br><br>
""", unsafe_allow_html=True)
        

        with st.expander("Environment, Domain and Constraints(Bounding Function) 🌅", expanded=True):
            
            st.markdown("""
#### Environment would be the chess board as actions are made upon and based on it 🎲
#### Domain would be all possible states that we consider while placing Queens (Shown in steps below) ⬇️
#### Constraints a.k.a Bounding Function would be not having 2 queens in same row, column and diagonals 📉""")

        st.write("""
<br><br>
""", unsafe_allow_html=True)

        with st.expander("Time and Space Complexity of the algo ⏳👽", expanded=True):
            
            st.markdown("""
#### This is based on the code snippet given above 🔼
####  📝 N is the number of Queens to be placed
#### ⏱️ Time Complexity 
###### Every base in the statespace tree after construction would have nodes which have n children
###### as we know the total depth of the tree is N
###### so total possible states passed by is (N^(N+1) - 1)/(N-1)
###### which after removal of constants will give us N^N
###### then since we go through all N columns... it should be considered as well
###### Atlast, over the constraint part  since we have to traverse through sets on search
###### Thats another 3N
###### in total its O(N^N * N * N) = O(N^(N+2)) = O(N^N) 😃

#### ⏱️ Space Complexity
###### we are using a stack under the hood for recursive calls(backtracking)
###### that's of depth N at max so its an N here
###### then we use 3 sets that would be of length N
###### so its N*3 since we have three sets
###### In total, O(N+3N) = O(N) 😃
""")

        st.write("""
<br><br>
""", unsafe_allow_html=True)

        solution_board = [["⬜️"]*number_of_queens for i in range(number_of_queens)]
        
        # Create the table
        st.markdown("##### Initial Chess Board")
        st.dataframe(data=solution_board)

        sol_list, solutions = nqueens.nQueensAllSolutions(number_of_queens) # n is passed and solutions are returned

        st.write("""
<br><br>
""", unsafe_allow_html=True)

        with st.expander("Solutions", expanded=True):
            for cnt in sol_list:
                holder = list()
                for i in solutions[cnt]:
                    inter = list()
                    for j in i:
                        if j == ".":
                            inter.append("⬜️")
                        else:
                            inter.append("🟧")
                    holder.append(inter)
                st.dataframe(data=holder)
                
                
        st.write("""
<br><br>
""", unsafe_allow_html=True)

        st.markdown("### 👋 Check on all moves made")

        for cnt, solution in enumerate(solutions):
            # replacing "." with "⬜️" and "Q" with "🟧"
            
            st.write("""
<br><br>
""", unsafe_allow_html=True)
            st.markdown(F"##### 🎯 Move {cnt+1}")
            st.markdown(("##### 😃✅ Valid Solution"
                        if cnt in sol_list else
                        "#####  🤔🥱 Haven't reached the solution yet")
                        )
            
            holder = list()
            
            for i in solution:
                inter = list()
                for j in i:
                    if j == ".":
                        inter.append("⬜️")
                    else:
                        inter.append("🟧")
                holder.append(inter)
            
            st.dataframe(data=holder)

        st.write("""
<br><br><br>
""", unsafe_allow_html=True)
        
        st.markdown("### 🙌 All possible moves have been made, <br><br>👋👋 Byeeeee. 😄", unsafe_allow_html=True)