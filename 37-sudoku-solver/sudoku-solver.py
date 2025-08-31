class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
      
        row, col, cell = [0] * 9, [0] * 9, [0] * 9
        empty = set()
        for i, j in product(range(9), repeat = 2):
            k = i - i % 3 + j // 3
            if board[i][j] == '.':
                empty.add((i, j, k))
            else:
                mask = 1 << int(board[i][j])
                row[i] |= mask
                col[j] |= mask
                cell[k] |= mask


        def bt():
            if not empty:
                return True
            # Select an empty cell with the most digits used
            max_cnt_num = 0
            for ii, jj, kk in empty:
                # cnt_num - number of digits used
                cnt_num = (row[ii] | col[jj] | cell[kk]).bit_count()
                if cnt_num > max_cnt_num:
                    max_cnt_num = cnt_num
                    i, j, k = ii, jj, kk

            mask = 1
            empty.remove((i, j, k))
            for n in '123456789':
                mask <<= 1
                if mask & row[i] or mask & col[j] or mask & cell[k]:
                    continue
                row[i] |= mask
                col[j] |= mask
                cell[k] |= mask
                if bt():
                    board[i][j] = n
                    return True
                row[i] ^= mask
                col[j] ^= mask
                cell[k] ^= mask
            empty.add((i, j, k))
            return False
            
        bt()