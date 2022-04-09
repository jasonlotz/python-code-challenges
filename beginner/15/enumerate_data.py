names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()

FIXED_WIDTH = 11


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""

    zipped_list = zip(names, countries)

    count = 0

    for item in zipped_list:
        count += 1
        padding = (FIXED_WIDTH - len(item[0])) * ' '
        print(f'{count}. {item[0]}{padding}{item[1]}')
