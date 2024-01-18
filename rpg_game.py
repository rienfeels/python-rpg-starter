class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
#^made a class character and initialized self, name, health, and power.^
    def attack(self, target):
        target.health -= self.power
        print("%s does %d damage." % (self.name, self.power))
#^Created an attack method that subtracts the targets health based on self power.^
    def alive(self):
        return self.health > 0
#Created an alive class that keeps self alive as long as health is greater than zero.^
    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))
#^Created a print status method that prints a string listing the characters health and power.^

class Hero(Character):
    def __init__(self):
        super().__init__( name= "hero", health=10, power=5)
#^Created a hero class that passes through the character methods, and sets the heros name, health and power.^        

class Goblin(Character):
    def __init__(self):
        super().__init__(name= "goblin", health=6, power=2)
#Created a goblin class that works the same way as the hero class.^

def main():
    hero = Hero()
    goblin = Goblin()
#^Created the main function with hero and goblin^
    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
#^started the while loop that prints the hero and goblins print status while theyre alive.^    

        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end="")
        user_input = input()
#^Prints out the game options.^
        if user_input == "1":
            hero.attack(goblin)
            if not goblin.alive():
                print("The goblin is dead.")
#^If input is 1 the hero attacks, if goblin is dead print he's dead.^                
        elif user_input == "2":
            pass
#^else if input is 2 then pass turn.^        
        elif user_input == "3":
            print("Goodbye.")
            break
#^else if input is 3 then end game.^        
        else:
            print("Invalid input %r" % user_input)
#^else if input is invalid then print a string saying so.^
        if goblin.alive():
            goblin.attack(hero)
            if not hero.alive():
                print("You are dead.")
#^If the goblin is alive he will attack the hero. If the hero is not alive then print a string saying so.^
if __name__ == "__main__":
    main()
#^This block of code will only run if the script is executed directly^