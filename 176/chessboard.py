WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    half_size = size // 2

    for _ in range(half_size):
        print(f'{WHITE}{BLACK}' * half_size)
        print(f'{BLACK}{WHITE}' * half_size)
