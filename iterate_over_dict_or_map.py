# create a python dictionary 
statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
print('List Of given capitals:\n')

for capital in statesAndCapitals.values():
    print(capital)

statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
keys = statesAndCapitals.keys()
print(keys)

statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
print('List Of given states:\n')

# Iterating over keys
for state in statesAndCapitals:
    print(state)

statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}

for key, value in statesAndCapitals.items():
    print(f"{key}: {value}")

statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
map_keys = map(statesAndCapitals.get, statesAndCapitals)
for key in map_keys:
    print(key)

statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
for state, capital in zip(statesAndCapitals.keys(), statesAndCapitals.values()):
    print(f'The capital of {state} is {capital}')            