import random

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print("%s does %d damage." % (self.name, self.power))

    def alive(self):
        return self.health > 0

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

    def swap_power(self, other):
        self.power, other.power = other.power, self.power
        print("%s and %s swap powers for one turn!" % (self.name, other.name))


class Hero(Character):
    def __init__(self, name, coins=20):
        super().__init__(name, health=10, power=5)
        self.coins = coins
        self.items = []

    def buy(self, item):
        if self.coins >= item.cost:
            self.coins -= item.cost
            self.items.append(item)
            print("%s bought %s for %d coins." % (self.name, item.name, item.cost))
        else:
            print("Not enough coins to buy %s." % item.name)

    def use_item(self, item, target):
        if item in self.items:
            item.apply(target)
            print("%s used %s during battle!" % (self.name, item.name))
            self.items.remove(item)
        else:
            print("%s doesn't have %s in their inventory." % (self.name, item.name))


class Enemy(Character):
    def __init__(self, name, bounty, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.bounty = bounty


class Goblin(Enemy):
    def __init__(self, name):
        super().__init__(name, bounty=5, health=6, power=2)


class Shadow(Enemy):
    def __init__(self, name):
        super().__init__(name, bounty=6, health=1, power=10)


class Zombie(Enemy):
    def __init__(self, name):
        super().__init__(name, bounty=7, health=2, power=5)


class Wizard(Enemy):
    def __init__(self, name):
        super().__init__(name, bounty=8, health=8, power=3)
        self.magic_power = 5

    def attack(self, target):
        if random.random() < 0.3:  # 30% chance to cast a magic attack
            print("%s casts a magic attack!" % self.name)
            target.health -= self.magic_power
        else:
            super().attack(target)


class Archer(Enemy):
    def __init__(self, name):
        super().__init__(name, bounty=9, health=7, power=4)
        self.accuracy = 0.8  # 80% accuracy

    def attack(self, target):
        if random.random() < self.accuracy:
            super().attack(target)
        else:
            print("%s's arrow missed!" % self.name)


class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def apply(self, target):
        pass


class Tonic(Item):
    def __init__(self):
        super().__init__("Tonic", cost=5)

    def apply(self, target):
        target.health += 2


class Sword(Item):
    def __init__(self):
        super().__init__("Sword", cost=8)

    def apply(self, target):
        target.power += 2


class Store:
    items = {"Tonic": Tonic, "Sword": Sword}

    @classmethod
    def do_shopping(cls, hero):
        print("Welcome to the store! Your current balance: %d coins." % hero.coins)
        print("Available items:")
        for item_name, item_class in cls.items.items():
            item = item_class()
            print("%s - Cost: %d coins" % (item_name, item.cost))

        print("Enter the item you want to buy (or 'exit' to leave the store):")
        item_choice = input().capitalize()

        if item_choice.lower() == 'exit':
            print("You left the store.")
        elif item_choice in cls.items:
            item = cls.items[item_choice]()
            hero.buy(item)
        else:
            print("Invalid item choice.")


class Battle:
    @staticmethod
    def do_battle(hero, enemy):
        print(f"A wild {enemy.name} appears!")

        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()

            print("What do you want to do?")
            print("1. Fight")
            print("2. Do nothing")
            print("3. Use item")
            print("4. Swap power")
            print("> ", end="")
            user_input = input()

            if user_input == "1":
                hero.attack(enemy)
                if not enemy.alive():
                    print(f"The {enemy.name} is defeated.")
                    hero.coins += enemy.bounty
            elif user_input == "2":
                pass
            elif user_input == "3":
                Store.do_shopping(hero)
            elif user_input == "4":
                Battle.swap_power(hero, enemy)
            else:
                print("Invalid input %r" % user_input)

            if enemy.alive():
                enemy.attack(hero)
                if not hero.alive():
                    print("You are dead.")

    @staticmethod
    def swap_power(character1, character2):
        character1.swap_power(character2)


def main():
    hero = Hero("Spider-man")
    goblin = Goblin("Green goblin")
    shadow = Shadow("Shady")
    zombie = Zombie("Walking Dead")
    wizard = Wizard("Evil Wizard")
    archer = Archer("Sharpshooter")

    enemies = [goblin, shadow, zombie, wizard, archer]

    while hero.alive() and any(enemy.alive() for enemy in enemies):
        remaining_enemies = [enemy for enemy in enemies if enemy.alive()]

        if remaining_enemies:
            current_enemy = random.choice(remaining_enemies)
            Battle.do_battle(hero, current_enemy)
        else:
            print("Congratulations! You defeated all enemies.")
            break

    if not any(enemy.alive() for enemy in enemies):
        print("Congratulations! You defeated all enemies.")


if __name__ == "__main__":
    main()
