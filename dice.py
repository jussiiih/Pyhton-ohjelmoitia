import random

class Dice:

    def __init__ (self, sides, current):
        self.sides = sides
        self.current = current

    def roll (self):
        self.current= random.randint(1, self.sides)


    def __str__ (self):
        return f'Current value is {self.current}'

class D3(Dice):
    def __init__(self):
        super().__init__(3,1)

class D4(Dice):
    def __init__(self):
        super().__init__(4,1)

class D6(Dice):
    def __init__(self):
        super().__init__(6,1)

class D8(Dice):
    def __init__(self):
        super().__init__(8,1)

class D10(Dice):
    def __init__(self):
        super().__init__(10,1)

class D12(Dice):
    def __init__(self):
        super().__init__(12,1)

class D20(Dice):
    def __init__(self):
        super().__init__(20,1)

class DiceCup:
    def __init__ (self):
        self.dicelist = []
        self.sum = 0
        self.result = ''

    def roll (self):
        self.sum = 0
        for dice in self.dicelist:
            dice.roll()
            self.sum += dice.current
            self.result += str(dice.current) + '+'
#        self.result += "=" + str(self.sum)

    def add_dice(self, dice):
        self.dicelist.append(dice)

    def remove_dice (self, dice):
        self.dicelist.remove(dice)
    
    def __str__(self):
        modified = self.result[0:len(self.result)-1]
        return f'{modified}={self.sum}'

# my_dice = D3()
# my_dice.roll()

my_dicecup = DiceCup()
my_dicecup.add_dice(D3())
my_dicecup.add_dice(D3())
my_dicecup.add_dice(D3())
my_dicecup.add_dice(D3())
my_dicecup.add_dice(D20())
my_dicecup.roll()
print(my_dicecup)
