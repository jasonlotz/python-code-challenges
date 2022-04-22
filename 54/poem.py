from multiprocessing.context import SpawnContext
from sre_constants import IN
from unittest import skip


INDENTS = 4


def print_hanging_indents(poem):
    new_paragraph = False

    # Remove leading white space
    for line in poem.splitlines():
        line = line.lstrip()

        if line == '':
            new_paragraph = True
            continue

        if new_paragraph is True:
            print(line)
            new_paragraph = False
        else:
            print((' ' * INDENTS) + line)