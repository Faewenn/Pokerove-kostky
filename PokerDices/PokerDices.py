import random

class Player:
    def __init__(self) -> None:
        self.dices = [random.randint(1, 6) for i in range(5)]
        self.strength_name, self.strength = self.get_strength()
    
    def __repr__(self):
        return str(self.dices) + f" -> {self.strength_name} ({self.strength})"

    def __eq__(self, other: object) -> bool:
        return self.strength == other.strength

    def __gt__(self, other) -> bool:
        return self.strength > other.strength

    def __lt__(self, other) -> bool:
        return self.strength < other.strength

    def roll_again(self, position):
        assert isinstance(position, int)  # pozice není typu int
        assert 0 <= position <= 5  # zadaná pozice je mimo rozsah
        
        self.dices[position] = random.randint(1,6)
        self.strength_name, self.strength = self.get_strength()


    def get_strength(self):
        dices = self.dices.copy()

        # Five of a Kind
        bools = [dices.count(i) == 5 for i in range(1,7)]
        if any(bools):
            return "Five of a Kind", 1000000000 * (bools.index(True) + 1)

        # Four of a Kind
        bools = [dices.count(i) == 4 for i in range(1,7)]
        if any(bools):
            return "Four of a Kind", 100000000 * (bools.index(True) + 1)

        # Full House
        bools = [dices.count(i) == 2 and dices.count(j) == 3 and i != j for i in range(1,7) for j in range(1, 7)]
        if any(bools):
            i, j = divmod(bools.index(True) + 1, 6)
            if j == 0:
                j = 6
                i -= 1
            return "Full house", 10000000 * j + 1000000 * (i + 1)

        # Vyšší postupka
        if all(i in dices for i in range(2,7)):
            return "Higher Straight", 900000

        # Niší postupka
        if all(i in dices for i in range(1,6)):
            return "Lower Straight", 800000

        # Three of a Kind
        bools = [dices.count(i) == 3 for i in range(1,7)]
        if any(bools):
            return "Three of a Kind", 100000 * (bools.index(True) + 1)

        # Two pairs
        bools = [dices.count(i) == 2 and dices.count(j) == 2 and i != j for i in range(1,7) for j in range(1, 7)]
        if any(bools):
            i, j = divmod(bools.index(True) + 1, 6)
            if j == 0:
                j = 6
                i -= 1
            return "Two pairs", 1000 * j + 100 * (i + 1)

        # Pair
        bools = [dices.count(i) == 2 for i in range(1,7)]
        if any(bools):
            return "One pair", 10 * (bools.index(True) + 1)
            
        return "High card", max(dices)

    def get_strengthPositions(self):
        dices = self.dices.copy()

        # Five of a Kind
        for i in range(1, 7):
            if dices.count(i) == 5:
                return [False for j in range(5)] 


        # Four of a Kind
        for i in range(1, 7):
            if dices.count(i) == 4:
                indexes = [True for j in range(5)] 
                for k, dice in enumerate(dices):
                    if dice == i:
                        indexes[k] = False
                
                return indexes


        # Full House
        if any([dices.count(i) == 2 and dices.count(j) == 3 and i != j for i in range(1,7) for j in range(1, 7)]):
            return [False for j in range(5)] 


        # Postupka
        if all(i in dices for i in range(2,7)) or all(i in dices for i in range(1,6)):
            return [False for j in range(5)]

        # Three of a Kind
        for i in range(1, 7):
            if dices.count(i) == 3:
                indexes = [True for j in range(5)] 
                for k, dice in enumerate(dices):
                    if dice == i:
                        indexes[k] = False
                
                return indexes

        # Two pairs
        for i in range(1, 7):
            for j in range(1, 7):
                if j == i:
                    continue

                if dices.count(i) == 2 and dices.count(j) == 2:
                    indexes = [True for j in range(5)] 
                    for k, dice in enumerate(dices):
                        if dice == i or dice == j:
                            indexes[k] = False
                    
                    return indexes



        # Pair
        for i in range(1, 7):
            if dices.count(i) == 2:
                indexes = [True for j in range(5)] 
                for k, dice in enumerate(dices):
                    if dice == i:
                        indexes[k] = False
                
                return indexes

        for i in range(7, 0, -1):
            if i in dices:
                indexes = [True for j in range(5)]
                indexes[dices.index(i)] = False
                return indexes




