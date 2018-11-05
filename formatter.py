import csv

types = {}
pokes = []
with open('pokemon.csv', 'r') as src_file:
    pokereader = csv.reader(src_file)
    for pokemon in pokereader:
        name = pokemon[1]
        type1 = pokemon[2]
        type2 = pokemon[3]
        if type1 not in types:
            types[type1] = []
        types[type1].append(name)

        if type2 != '' and type2 is not None:
            if type2 not in types:
                types[type2] = []
            types[type2].append(name)
        pokes.append(name)

with open('pokemon_nodes.csv', 'w') as dst_file:
    pokewriter = csv.writer(dst_file)
    pokewriter.writerow(['Name'])
    for p in pokes:
        pokewriter.writerow([p])

with open('pokemon_edges.csv', 'w') as dst_file:
    pokewriter = csv.writer(dst_file)
    pokewriter.writerow(['Source', 'Target', 'Type', 'Pokemon Type'])
    for t in types:
        connected_pokes = types[t]
        for i in range(len(connected_pokes) - 1):
            for j in range(i+1, len(connected_pokes)):
                pokewriter.writerow([connected_pokes[i], connected_pokes[j], 'Undirected', t])

