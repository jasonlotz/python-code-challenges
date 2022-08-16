def flatten(list_of_lists):
    result = []

    def inner_flattern(v):
        """inner_flattern - recursive"""
        if len(v) == 0:
            return

        if isinstance(v[0], list) or isinstance(v[0], tuple):
            inner_flattern(v[0])
        else:
            result.append(v[0])

        inner_flattern(v[1:])

    # - results
    inner_flattern(list_of_lists)
    return result
