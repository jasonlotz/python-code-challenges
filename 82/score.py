def flatten(list_of_lists):
    '''Use recursion: if list or tuple call self = go one level deeper,
       if base case return it. Using yield (generator) for convenience'''
    for item in list_of_lists:
        if type(item) in (list, tuple):
            yield from flatten(item)
        else:
            yield item
