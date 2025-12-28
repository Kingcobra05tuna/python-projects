from random import randint, choice
from time import sleep

# rooms
rooms = [
    "a room with glowing walls.",
    "a forest without grass.",
    "a burning village.",
    "an abandoned facility.",
    "an old house.",
    "an apartment."
]

# monsters
monsters = {
    "Goblin": {'Health': 25},
    "Giant": {'Health': 50},
    "Snake": {'Health': 15},
    "Zombie": {'Health': 30},
    "Skeleton": {'Health': 20},
    "Mouse": {'Health': 10},
    "Dragon": {'Health': 90}
}

MAXHEALTH_P = 100
speedy = False
simulate = False


class Creature:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, player):
        dmg = randint(5, 20)
        dmg = randomize(dmg, 5)
        print(f"[HIT] {self.name} dealt {dmg} damage to {player.name}. "
              f"{player.name} has {max(0, player.health - dmg)} hp left.")
        player.handle_attack(dmg)

    def handle_attack(self, dmg):
        dmg = max(round(dmg / 10), dmg)
        self.health -= dmg
        return self.health <= 0


class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.HealAmount = 20
        self.Damage = 15
        self.CritDamage = 30
        self.killCount = 0
        self.totalHealAmount = 0
        self.numberOfEncounters = 0

    def encounter(self):
        name = choice(list(monsters.keys()))
        health = randomize(monsters[name]['Health'], 5)
        creature = Creature(name, health)

        self.numberOfEncounters += 1
        print(f"{self.name} encountered {creature.name}. It has {creature.health} HP.")

        while self.health > 0 and creature.health > 0:
            if simulate:
                move = "a"
            else:
                move = input(f"[>] Do {self.name} want to attack (a) or flee (f)? ").strip().lower()

            if move == "a":
                self.attack(creature)
            else:
                print(f"{self.name} escaped.")
                break

            if creature.health > 0:
                wait(0.4)
                print(f"It's {creature.name}'s turn!")
                wait(0.4)
                creature.attack(self)

    def explore(self):
        print(f"---------- {self.name} entered {choice(rooms)} ----------")

        if randint(1, 100) <= 40 and self.health < MAXHEALTH_P:
            h = randomize(self.HealAmount, self.HealAmount // 5)
            self.health = min(self.health + h, MAXHEALTH_P)
            self.totalHealAmount += h
            print(f"+++ {self.name} healed {h} hp! New hp: {self.health} +++")

        if randint(1, 100) <= 55:
            self.encounter()
        else:
            print(f"{self.name} found nothing.")

    def attack(self, creature):
        base = 0
        if self.health < creature.health:
            base += randomize(5, 2)

        if randint(1, 100) <= 20:
            base += self.CritDamage
            print("\n### >> CRITICAL HIT! << ###\n")
            wait(0.2)
        else:
            base += self.Damage

        dmg = randomize(base, base // 5)
        print(f"{self.name} dealt {dmg} damage to {creature.name}. "
              f"It has {max(0, creature.health - dmg)} hp left.")

        if creature.handle_attack(dmg):
            print(f"{self.name} killed {creature.name}!")
            self.killCount += 1

    def handle_attack(self, dmg):
        self.health -= max(0, dmg)
        if self.health <= 0:
            self.showStats()
            return True

    def showStats(self):
        print(f"\n{self.name} died!\n")
        wait(0.3)
        print("----- Stats -----")
        print(f"Encounters: {self.numberOfEncounters}")
        print(f"Kills: {self.killCount}")
        print(f"Total heal: {self.totalHealAmount} hp")


def randomize(num, variance):
    return max(0, randint(num - variance, num + variance))


def wait(duration):
    if speedy:
        sleep(duration)


def main():
    global speedy, simulate

    print("********** Welcome to the Dungeon! **********")
    name = input("[>] What is your name?: ").strip().capitalize()
    player = Player(name, MAXHEALTH_P)

    speedy_sel = input("[>] Enable delays? (y/n): ").strip().lower()[0]
    if speedy_sel == "y":
        speedy = True

    sim_sel = input("[>] Do you want to simulate the game? (y/n): ").strip().lower()[0]
    if sim_sel == "y":
        simulate = True
        print(">>> SIMULATION MODE ACTIVE <<<\n")

    while True:
        if simulate:
            action = "e"
        else:
            action = input("[>] Explore (e) or leave (l)?: ").strip().lower()[0]

        print()

        if action == "e":
            player.explore()
            if simulate and player.health <= 0:
                break
        else:
            print("You left the dungeon.")
            player.showStats()
            break


if __name__ == "__main__":
    main()
