"""
--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
"""


class BingoBoard:

    def __init__(self, numbers):
        self.numbers = [int(n) for n in numbers.replace("\n", " ").split()]
        self.marked = set()

    def mark(self, n):
        if n in self.numbers:
            self.marked.add(n)
            return self.check_win()
        return False

    def get_score(self):
        return sum(self.marked.symmetric_difference(self.numbers))

    def check_win(self):
        return self.check_rows() or self.check_columns()

    def check_rows(self):
        for i in range(0, 21, 5):
            if self.marked.issuperset(self.numbers[i:i + 5]):
                return True
        return False

    def check_columns(self):
        for i in range(5):
            if self.marked.issuperset(self.numbers[i::5]):
                return True
        return False


def get_boards_and_nums(filename):
    with open(filename) as file:
        data = file.read().split("\n\n")
    drawn_numbers = [int(n) for n in data[0].split(",")]
    # so we can pop from the start
    drawn_numbers.reverse()
    boards = [BingoBoard(numbers) for numbers in data[1:]]
    return drawn_numbers, boards


def main():
    drawn_numbers, boards = get_boards_and_nums('../inputs/four_puzzle_one_input.txt')
    # while we have numbers to draw
    while drawn_numbers:
        n = drawn_numbers.pop()
        # keep track of boards to remove when they win
        boards_to_remove = set()
        for board in boards:
            win = board.mark(n)
            # if a board wins
            if win:
                #  and there is more than one board that can be played
                if len(boards) > 1:
                    # add board to boards to remove
                    boards_to_remove.add(board)
                else:
                    # otherwise print the score
                    print(board.get_score() * n)
        # remove the boards
        boards = [board for board in boards if board not in boards_to_remove]


if __name__ == '__main__':
    main()
