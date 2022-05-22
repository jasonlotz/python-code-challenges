from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)

    for line in data.splitlines()[1:]:
        split_line = line.split(',')
        first_name = split_line[1]
        last_name = split_line[0]
        country = split_line[2]

        countries[country].append(f'{first_name} {last_name}')

    return countries
