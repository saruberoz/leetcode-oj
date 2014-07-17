
# I used a a list of lists of 1 length string for my data structure of the board
# using dfs for no_wrap case and backtracing for wrap case.


import sys

class Solution:
    def exist_no_wrap(self, board, word):
        ''' Algorithm to check word exist on board for wrap case
        @param board, a list of lists of 1 length string
        @param word, a string
        @return status of found/not-found, start of the find, end of the find
        '''
        start, end = (0, 0), (0, 0)
        if not word:
            return False, start, end

        max_row, max_col = len(board), len(board[0])
        if len(word) > max(len(board), len(board[0])):
            return False, start, end
        for r in range(0, max_row):
            for c in range(0, max_col):
                if board[r][c] == word[0]:
                    start = (r, c)
                    if len(word) == 1:
                        return True, start, start
                    status, end = self.dfs(board, r, c, word[1:])
                    if status:
                        return True, start, end

        return False, start, end

    def exist_wrap(self, board, word):
        start, end = (0, 0), (0, 0)
        if not word:
            return False, start, end
        max_row, max_col = len(board), len(board[0])
        for r in range(0, max_row):
            for c in range(0, max_col):
                if board[r][c] == word[0]:
                    start = r, c
                    if len(word) == 1:
                        return True, start, start
                    status, end = self.backtrace(board, r, c, word)
                    if status:
                        return True, start, end

        return False, start, end

    def backtrace(self, board, r, c, word):
        ''' Algorithm using spanning backtrace to check if the word occur on the board
            @param board, a list of lists of 1 length string
            @param r, which row checking should be done
            @param c, which col checking should be done
            @param word, a string to be check (continuing from the last checked character)
            @return status found or not, end where the last char of word is found
        '''
        max_row, max_col = len(board), len(board[0])
        max_diagonal = max_row*max_col
        # span to the right from the starting point, and check if the result contains the searched string
        right_result =  [(r, x % max_col) for x in range(c, c + max_col)]
        resulting_string = '' # always reset the resulting string
        for p in right_result:
            resulting_string += board[p[0]][p[1]]
            if word == resulting_string:
                return True, (p[0], p[1])
        # span to left from the starting point and check if the result contain the searched string
        left_result =  [(r, x % max_col) for x in range(c, c - max_col, -1)]
        resulting_string = '' # always reset the resulting string
        for p in left_result:
            resulting_string += board[p[0]][p[1]]
            if word == resulting_string:
                return True, (p[0], p[1])
        # span up from the starting point and check if the result contain the searched string
        up_result =  [(x % max_row, c) for x in range(r, r - max_row, -1)]
        resulting_string = '' # always reset the resulting string
        for p in up_result:
            resulting_string += board[p[0]][p[1]]
            if word == resulting_string:
                return True, (p[0], p[1])
        # span down from the starting point and check if the result contain the searched string
        down_result =  [(x % max_row, c) for x in range(r, r + max_row)]
        resulting_string = '' # always reset the resulting string
        for p in down_result:
            resulting_string += board[p[0]][p[1]]
            if word == resulting_string:
                return True, (p[0], p[1])
        # span to top right from the starting point and check if the result contain the searched string
        to_top_right_row = [(x % max_row) for x in range(r, r - max_diagonal, -1)]
        to_top_right_col = [(x % max_col) for x in range(c, c + max_diagonal)]
        resulting_string = '' # always reset the resulting string
        for i in range(0, max_diagonal):
            resulting_string += board[to_top_right_row[i]][to_top_right_col[i]]
            if word == resulting_string:
                return True, (to_top_right_row[i], to_top_right_col[i])
        # span to top left from the starting point and check if the result contain the searched string
        to_top_left_row = [(x % max_row) for x in range(r, r - max_diagonal, -1)]
        to_top_left_col = [(x % max_col) for x in range(c, c - max_diagonal, -1)]
        resulting_string = '' # always reset the resulting string
        for i in range(0, max_diagonal):
            resulting_string += board[to_top_left_row[i]][to_top_left_col[i]]
            if word == resulting_string:
                return True, (to_top_left_row[i], to_top_left_col[i])
        # span to top left from the starting point and check if the result contain the searched string
        to_bot_left_row = [(x % max_row) for x in range(r, r + max_diagonal)]
        to_bot_left_col = [(x % max_col) for x in range(c, c - max_diagonal, -1)]
        resulting_string = '' # always reset the resulting string
        for i in range(0, max_diagonal):
            resulting_string += board[to_bot_left_row[i]][to_bot_left_col[i]]
            if word == resulting_string:
                return True, (to_bot_left_row[i], to_bot_left_col[i])
        # span to bot right from the starting point and check if the result contain the searched string
        to_bot_right_row = [(x % max_row) for x in range(r, r + max_diagonal)]
        to_bot_right_col = [(x % max_col) for x in range(c, c + max_diagonal)]
        resulting_string = '' # always reset the resulting string
        for i in range(0, max_diagonal):
            resulting_string += board[to_bot_right_row[i]][to_bot_right_col[i]]
            if word == resulting_string:
                return True, (to_bot_right_row[i], to_bot_right_col[i])

        return False, (0, 0)


    def dfs(self, board, r, c, word):
        ''' Algorithm using DFS to check if the word occur on the board
            @param board, a list of lists of 1 length string
            @param r, which row checking should be done
            @param c, which col checking should be done
            @param word, a string to be check (continuing from the last checked character)
            @return status found or not, end where the last char of word is found
        '''
        # self.print_board(board) # This is to see the algo step by step
        max_row, max_col = len(board), len(board[0])
        if len(word) == 0: # when the all the char in word are checked
            return True, (r, c) # save the end
        # Bottom to Top
        if (r > 0 and board[r - 1][c] == word[0]):
            ch, board[r][c] = board[r][c], '*'
            status, end = self.dfs(board, r - 1, c, word[1:])
            board[r][c] = ch # reset the char after done
            if status : return True, end
        # Top to Bottom
        if (r < max_row - 1 and board[r + 1][c] == word[0]):
            ch, board[r][c] = board[r][c], '*'
            status, end = self.dfs(board, r + 1, c, word[1:])
            board[r][c] = ch # reset the char after done
            if status: return True, end
        # Left to Right
        if (c < max_col - 1 and board[r][c+1] == word[0]):
            ch, board[r][c] = board[r][c], '*'
            status, end = self.dfs(board, r, c + 1, word[1:])
            board[r][c] = ch # reset the char after done
            if status: return True, end
        # Right to Left
        if (c > 0 and board[r][c - 1] == word[0]):
            ch, board[r][c] = board[r][c], '*'
            status, end = self.dfs(board, r, c - 1, word[1:])
            board[r][c] = ch # reset the char after done
            if status: return True, end
        # Diagonal down right
        if (r < max_row - 1 and c < max_col - 1 and board[r + 1][c + 1] == word[0]):
            ch, board[r][c] = board[r][c], '*'
            status, end = self.dfs(board, r + 1, c + 1, word[1:])
            board[r][c] = ch # reset the char after done
            if status: return True, end
        # Diagonal top right
        if (r > 0 and c < max_col - 1 and board[r - 1][c + 1] == word[0]):
            ch, board[r][c] = board[r][c], '*'
            status, end = self.dfs(board, r - 1, c + 1, word[1:])
            board[r][c] = ch # reset the char after done
            if status: return True, end
        # Diagonal top left
        if (r > 0 and c > 0 and board[r - 1][c - 1] == word[0]):
            ch, board[r][c] = board[r][c], '*'
            status, end = self.dfs(board, r - 1, c - 1, word[1:])
            board[r][c] = ch # reset the char after done
            if status: return True, end
        # Diagonal down right
        if (r < max_row - 1 and c > 0 and board[r + 1] [c - 1] == word[0]):
            ch, board[r][c] = board[r][c], '*'
            status, end = self.dfs(board, r + 1, c - 1, word[1:])
            board[r][c] = ch # reset the char after done
            if status: return True, end

        return False, (r, c)


    def run(self, board, word_list, wrap):
        ''' For running the app
        @param board, a list of lists of 1 length of string/char
        @param word_list, list of word to be search on the board
        @param wrap, boolean value of wrap or no-wrap
        '''
        for word in word_list:
            if wrap:
                status, start, end = self.exist_wrap(board, word)
                if status:
                    print '{} {}'.format(start, end)
                else:
                    print 'NOT FOUND'
            else:
                status, start, end = self.exist_no_wrap(board, word)
                if status:
                    print '{} {}'.format(start, end)
                else:
                    print 'NOT FOUND'


    def run_test_case(self):
        ''' Unit Test '''
        # no-wrap case
        board = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        word_list = ['fed', 'cab', 'gad', 'bid', 'high']
        expected = [True, False, False, False, False]
        for index in range(0, len(word_list)):
            status, start, end = self.exist_no_wrap(board, word_list[index])
            assert expected[index] == status, 'Fail no-wrap case {}'.format(index)
        # no-wrap case
        board = [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ]
        word_list = ['CFA', 'ABCD', 'SEE', 'ABCB','SE']
        expected = [True, True, True, False, True]
        for index in range(0, len(word_list)):
            status, start, end = self.exist_no_wrap(board, word_list[index])
            assert expected[index] == status, 'Fail no-wrap case {}, {}'.format(index, word_list[index])
        # wrap case
        board = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l']
        ]
        word_list = ['fed', 'cab', 'aeijbfg', 'lgec', 'high']
        expected = [True, True, True, True, False]
        for index in range(0, len(word_list)):
            status, start, end = self.exist_wrap(board, word_list[index])
            assert expected[index] == status, 'Fail wrap case {}, {}'.format(index, word_list[index])


    def print_board(self, board):
        ''' Prettify board printing
        @param board, a list of lists of 1 length string/char
        '''
        for i in range(0, len(board[0])+2):
            print "-",
        print '' # print newline
        for i in range(0, len(board)):
            print '|',
            for j in range(0, len(board[0])):
                print board[i][j],
            print '|',
            print '' # print newline
        for i in range(0, len(board[0])+2):
            print "-",
        print '' # print newline


if __name__ == "__main__":
    print 'Format of input data:'
    print '   N M'
    print '   N rows of M letters'
    print '   WRAP or NO_WRAP'
    print '   P'
    print '   P words with 1 word per lines\n'
    try:
        ###########################################
        # This is all reading input as the format #
        ###########################################
        line_1 = sys.stdin.readline()
        n, m = line_1.split(' ') # n and m type is str
        board = []
        for i in range(0, int(n)):
            board_string = sys.stdin.readline().rstrip('\n').lower() # this is to make case insensitive
            board.append(list(board_string)) # make the string a list of char for easier processing
        wrap = True if sys.stdin.readline().rstrip('\n').lower() == 'wrap' else False
        num_word = int(sys.stdin.readline())
        word_list = []
        for i in range(0, num_word):
            word_list.append(sys.stdin.readline().rstrip('\n').lower())
        ######################################
        # end of reading input as the format #
        ######################################

        solution = Solution()
        print 'N={}, M={}'.format(n, m)
        print 'Your board is'
        solution.print_board(board)
        print 'Wrap is {}'.format(wrap)
        print 'Number of word to be search in the board is {}'.format(num_word)
        print 'Word to be searched is {}'.format(word_list)
        print '\n'
        solution.run(board, word_list, wrap)

        print '\nRunning test case'
        solution.run_test_case()
    except Exception as e:
        raise e
        exit()
