import os


def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    num_lines = 0
    num_words = 0
    num_charc = 0

    with open(file_, 'r') as f:

        for line in f:
            num_lines += 1
            num_words += len(line.split())
            num_charc += len(line)

    return f'{num_lines} {num_words} {num_charc} {file_}'


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
