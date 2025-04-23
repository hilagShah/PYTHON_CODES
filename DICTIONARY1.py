wild_animals = {'Tiger' : 100,'Lion' : 101,'Leopard' : 102}
birds = {'Sparrow' : 103, 'Humming Bird' : 104,'Crow' : 105}
fishes = {'Tuna' : 106,'Pomphret' : 107,'Catfish' : 108}

combined = {**wild_animals,**birds,**fishes}
print(combined)

