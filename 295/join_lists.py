from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    result = []

    for list_element in lst_of_lst:
        for item in list_element:
            result.append(item)
        result.append(sep)

    # hacky way to remove the last separator
    if result:
        result.pop()
    else:
        result = None

    return result
