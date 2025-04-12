import random
gladiator_1 = {"hp":100, "damage":random.randint(1,5)}
gladiator_2 = {"hp":100, "damage":random.randint(1,5)}

def miss_chance():
    chance = random.randint(1,100)
    return chance > 10

while gladiator_1["hp"] or gladiator_2["hp"] > 0:
    if miss_chance():
        gladiator_2["hp"] -= gladiator_1["damage"]
        print("Gladiator 1 нанес удар", gladiator_1["damage"])
    else:
        print("Gladiator 1 промахнулся")
    if gladiator_2["hp"] <= 0:
        print("Gladiator 1 win!")
        break

    if miss_chance():
        gladiator_1["hp"] -= gladiator_2["damage"]
        print(f"Gladiator 2 нанес удар" , gladiator_2["damage"])
    else:
        print("Gladiator 2 промахнулся")
    if gladiator_1["hp"] <= 0:
        print("Gladiator 2 win!")
        break
        