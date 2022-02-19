cars = {}
cars['corola'] = "red"
cars['fit'] = "green"
cars['320'] = "black"

print(cars)
print(cars.keys())
# dict_keys(['corola','fit','320'])
cars.values()
# dict_values('red','green','black')
cars['corola']

people = dict(Wesley='Father', Mariana='Mother', Sarah='Baby')
print(people)

if 'Wesley' in people:
    print(people['Wesley'])

family = {
    'Wesley':'Father'
}

print(family)

for car in cars:
    print(car + " = " + cars[car])

for key, value in cars.items():
    print('-----------------')
    print(key + " = " + value)