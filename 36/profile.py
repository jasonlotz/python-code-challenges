def get_profile(name, age, *args, **kwargs):
    if not isinstance(age, int):
        raise ValueError
    if len(args) > 5:
        raise ValueError

    result = {
        'name': name,
        'age': age,
    }
    if args:
        result['sports'] = sorted(list(args))
    if kwargs:
        result['awards'] = kwargs

    return result
