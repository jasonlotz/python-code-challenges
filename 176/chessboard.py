from lib2to3.pgen2.token import NEWLINE


WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    repeat_count = int(size / 2)

    for line in range(size):
        if line % 2:
            print(f'{BLACK}{WHITE}' * repeat_count)
        else:
            print(f'{WHITE}{BLACK}' * repeat_count)
