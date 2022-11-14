import json
import itertools


def calcul_chemin_BFS(adjacents, depart, arrivee):
    a_explorer = [depart]
    deja_collectes = [depart]
    chemins = {depart: [depart]}

    while len(a_explorer) != 0:
        courant = a_explorer.pop(0)

        if courant == arrivee:
            return chemins[arrivee]

        if courant in adjacents:
            for sommet in adjacents[courant]:
                if sommet not in deja_collectes:
                    a_explorer.append(sommet)
                    deja_collectes.append(sommet)
                    chemins[sommet] = chemins[courant] + [sommet]

    return None


def direct_cycle(adjascents, ingredients):

    if len(ingredients) < 2:
        print("Not enough ingredients")
        return []

    result = []

    i = 0
    while i < len(ingredients):
        if i == 0:
            path = calcul_chemin_BFS(adjascents, ingredients[i], ingredients[i + 1])
        elif i == len(ingredients) - 1:
            path = calcul_chemin_BFS(adjascents, ingredients[-1], ingredients[0])[
                1:
            ]  # [1:] to prevent the same ingredient from being mentioned twice
        else:
            path = calcul_chemin_BFS(adjascents, ingredients[i], ingredients[i + 1])[
                1:
            ]  # [1:] to prevent the same ingredient from being mentioned twice

        result += path
        i += 1

    return result


def shortest_cycle(adjascents, ingredients):
    all_perm = list(itertools.permutations(ingredients, len(ingredients)))

    shortest_path = all_perm[0]
    min_lenght = len(direct_cycle(adjascents, all_perm[0]))
    for i in range(1, len(all_perm)):
        length = len(direct_cycle(adjascents, all_perm[i]))
        if length < min_lenght:
            shortest_path = all_perm[i]

    return shortest_path


def mk_diagram(path):
    result = "digraph {"

    i = 0
    while i < len(path) - 1:
        result += f'\n "{path[i]}" -> "{path[i + 1]}"'
        i += 1

    result += "\n}"

    with open("output.dot", "w") as f:
        f.write(result)


with open("./json/favorise.json") as f:
    favorise = json.load(f)

ingredients = ["fraisier des bois", "framboisier", "cerisier", "cassis"]
smallest_garden = shortest_cycle(favorise, ingredients)
garden = direct_cycle(favorise, smallest_garden)
print(garden)

# mk_diagram(garden)
