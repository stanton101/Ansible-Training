words = "Why sometimes I have believed as many as six impossible things before breakfast".split()


print([len(word) for word in words])

lengths = []
for word in words:
    lengths.append(len(word))

print(lengths)

country_to_capital = {'United Kingdom': 'London',
                      'Brazil': 'Brasilia',
                      'Morocco': 'Rabat',
                      'Sweden': 'Stockholm'}
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
from pprint import pprint as pp
pp(capital_to_country)
words = ["hi", "hello", "foxtrot", "hotel"]
print({x[0]: x for x in words})