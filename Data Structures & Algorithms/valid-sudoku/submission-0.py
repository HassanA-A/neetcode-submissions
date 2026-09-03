class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Loop through each collumn and add to hash table
        #then have if statement if one has a frquency higher than 1 then board is invalid or if less than  or basically if not ==1
        # 
        rows = [
            set(),  # row 0
            set(),  # row 1
            set(),  
            set(),  
            set(),  
            set(),  
            set(),  
            set(),  
            set()  
            
        ]

        cols = [
            set(),  # column 0
            set(),  # column 1
            set(),  
            set(),  
            set(),  
            set(),  
            set(),  
            set(),  
            set()  
            
        ]

        boxes = [
            set(),  # box 0
            set(),  # box 1
            set(),  
            set(),  
            set(),  
            set(),  
            set(),  
            set(),  
            set()  
            
        ]        
        # If u want to look at each row its just i in board
        # If u want to look at each column [i]12345, 
        # If u want each square then u gotta do 
        
        
        for i in range(9):
            for x in range(9):
                if board[i][x] == ".":
                    continue
                
                row = i
                col = x
                box = (row // 3) * 3 + (col // 3)

                if (board[i][x] in rows[row] or board[i][x] in cols[col] or board[i][x] in boxes[box] ):
                    return False
                
                rows[row].add(board[i][x])
                cols[col].add(board[i][x])
                boxes[box].add(board[i][x])

        return True
                



            


        