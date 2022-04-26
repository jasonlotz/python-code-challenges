import itertools

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    sums = itertools.accumulate(sequence)
    
    return [round(accum / i, 2) for i, accum in enumerate(sums, start=1)]


if __name__ == '__main__':
   print(running_mean([1, 2, 3]))