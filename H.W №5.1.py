import random
class Gladiator:
    def __init__(self, name, hp, damage, crit_chance, miss_chance):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.crit_chance = crit_chance
        self.miss_chance = miss_chance
        self.abil_activate = False

    def use_ability(self):
        if random.randint(1, 100) > 50:
            self.abil_activate = True
            print(f"{self.name} уклонился")

    def attack(self, opponent):

        if random.randint(1,100) < self.miss_chance:
            print(f"{self.name} промахнулся")
            return


        if opponent.abil_activate:
            print(f"{opponent.name} уклонился")
            opponent.abil_activate = False
            return

        hit = random.randint (self.damage - 2, self.damage + 2)

        if random.randint(1, 100) < self.crit_chance:
            hit *= 2
            print(f"{self.name} нанёс крит удар")

        opponent.hp -= hit
        print(f"{self.name} нанес {hit} урона {opponent.name}")

        if opponent.hp < 0:
            opponent.hp = 0

gl_1 = Gladiator("maximus", 100, 5, 30, 15)
gl_2 = Gladiator("spartacus", 100, 5, 15, 30)

while gl_1.hp > 0 or gl_2.hp > 0:

    if random.randint(1, 100) <= 50:
        gl_2.use_ability()

    gl_1.attack(gl_2)
    print(f"Здоровье gl_2 составляет HP:{gl_2.hp}")

    if gl_2.hp <= 0:
        print("gl_1 Одержал победу!")
        break

    gl_2.attack(gl_1)
    print(f"Здоровье gl_1 составляет HP:{gl_1.hp}")

    if gl_1.hp <= 0:
        print("gl_2 Одержал победу!")
        break
