from usefull_data import adjascents


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


def shortest_cycle(adjascents, ingredients):

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


def mk_diagram(path):
    result = "digraph {"

    i = 0
    while i < len(path) - 1:
        result += f"\n '{path[i]}' -> '{path[i + 1]}'"
        i += 1

    result += "\n}"

    with open("output.dot", "w") as f:
        f.write(result)


ingredients = ["fraisier des bois", "framboisier", "cerisier"]
path = shortest_cycle(adjascents, ingredients)
print(path)
mk_diagram(path)
