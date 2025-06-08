1. 
Programmers use stubs which are temporary functions that simulate behaviour of the actual code, to test the entire system or big modules of the system ot enusre functionality without requiring the completed function. Usually the function is an API call, which they haven't finilised or don't have the key to. The stubs allow you to complete testing earlier and have a smoother intergration stage in your project.

2. Why is version control important.
Version control's important as it takes snapshot of your code through time and allows you to revert to previous versions if you make a mistake. It's also easier to collaborate with developers being able to create forks of the program in order to work on seperate "branches" or version of the control and then merge them back when they see fit. It also allows you to track every modification made to the codebase overtime.

3. Explain Code optimisation in software egineering
Code optimisation is the process of making a computer program more efficient and removing its intensity on the computer's resources. The goal is to make th program and performance of the code easier to run which allows lower hardwware to run your program better as it needs less resources. By making your program more accesible, it is more likely to succeed in it's point or purpose.

4. 
In A the classes themselves contain the print statement
```py
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, other_player, damage):
        print(f"{self.name} attacks {other_player.name} for {damage} damage!")
        other_player.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name}'s health is now {self.health}")


# Create two Player objects
alice = Player("Alice", 100)
bob = Player("Bob", 100)

# One player sends a message (method call) to another
alice.attack(bob, 25)
```
In B the response by the classes is returned and the returned statement is printed by other class functions.

b.
``` py
class Chest:
    def __init__(self, gold_amount):
        self.gold_amount = gold_amount
        self.is_open = False

    def open(self, player):
        if not self.is_open:
            print(f"{player.name} opens the chest and finds {self.gold_amount} gold!")
            player.collect_gold(self.gold_amount)
            self.is_open = True
        else:
            print("The chest is already empty.")

class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0

    def open_chest(self, chest):
        chest.open(self)  # Message passing: player sends message to chest

    def collect_gold(self, amount):
        self.gold += amount
        print(f"{self.name} now has {self.gold} gold.")


# Creating objects
player = Player("Lara")
treasure_chest = Chest(50)

# Interactions using message passing
player.open_chest(treasure_chest)   # Lara opens chest, chest gives her gold
player.open_chest(treasure_chest)
```


5. 
```py
def add(x,y):
    return x + y
print(add(5,7))
```

```py
print(" Welcome, Ali! \n Welcome, Ben! \n Welcome, Cat! \n Welcome, Doge! \n Welcome, Eggbert! \n Welcome, Fred! \n Welcome, Grod!")
```

```py
class Animal:
    def __init__(self,type_):
        self.sound = ""
        self.type = type_

    def make_sound(self):
        if self.type_ == "Dog":
            print("Dog goes woof")
        elif self.type_ == "Cat":
            print("Cat goes meow")
        elif self.type_ == "Cow":
            print("Cow goes moo")
        else:
            print("Unknown animal sound")

animals = [Animal("Dog"),Animal("Cow"),Animal("Cat")]
for a in animals:
    a.make_sound()

```

```py
words = ["hello", "world", "!"]
sentence = ""
print(sentence.join(words))

```

```py
fruit_stock = ["apple", "banana", "cherry"]
for i, item in enumerate(fruit_stock):
    print(i, item)
```