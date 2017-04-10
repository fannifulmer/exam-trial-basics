pirates = [
    {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
    {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
    {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
    {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
    {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

def pirate_counter(pirate = 'Name'):
    sum_name = ''
    for elements in pirate:
        if elements['gold'] > 15 or ['has_wooden_leg'] == True:
            sum_name += elements['Name']
    print(sum_name)
    
pirate_counter(pirates)

    
# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that
# - have wooden leg and
# - have more than 15 gold
