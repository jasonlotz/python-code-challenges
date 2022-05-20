from lib2to3.pgen2.token import NEWLINE


WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    repeat_count = int(size / 2)

    for line in range(0, size):
        if line % 2 == 0:
            print(f'{WHITE}{BLACK}' * repeat_count)
        else:
            print(f'{BLACK}{WHITE}' * repeat_count)
