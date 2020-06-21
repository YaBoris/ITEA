
list_country = ['Ukraine', 'Austria', 'Moldova', 'Germany', 'Kongo', 'Vietnam', 'Russia', 'USA']
dict_countries = {
    'China': 'Beijing',
    'Laos': 'Vientiane',
    'Ukraine': 'Kyiv',
    'Austria': 'Vena',
    'Russia': 'Moscow'
}

for country in list_country:
    if dict_countries.get(country):
        print(dict_countries.get(country))
