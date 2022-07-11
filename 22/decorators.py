from functools import wraps


def make_html(element):
    left_braket = f'<{element}>'
    right_braket = f'</{element}>'

    def decorate(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            text = func(*args, **kwargs)
            text = left_braket + text + right_braket
            return text

        return wrapped

    return decorate
