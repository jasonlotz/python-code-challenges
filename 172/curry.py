from functools import partial
import functools

# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places
rounder_int = partial(round, ndigits=0)
rounder_detailed = partial(round, ndigits=4)
