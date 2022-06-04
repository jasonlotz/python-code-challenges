import pytest

from workouts import print_workout_days


@pytest.mark.parametrize('input, expected', [
    ('upper', 'Mon, Thu\n'),
    ('lower', 'Tue, Fri\n'),
    ('body', 'Mon, Tue, Thu, Fri\n'),
    ('#1', 'Mon, Tue\n'),
    ('#2', 'Thu, Fri\n'),
    ('30', 'Wed\n'),
    ('min', 'Wed\n'),
    ('cardio', 'Wed\n'),
    ('nomatch', 'No matching workout\n'),
])
def test_print_workout_days(capsys, input, expected):
    print_workout_days(input)
    out, err = capsys.readouterr()
    assert out == expected
