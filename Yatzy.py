from os import pardir

class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        puntos = 0
        for die in dice:
            puntos += die
        return puntos
    
    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) == 5:
            return 50
        return 0
    
    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE)
    
    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * 2

    @staticmethod
    def threes(*dice):
        THREE = 3
        return dice.count(THREE) * 3
    
    def fours(self):
        FOUR = 4
        return self.dice.count(FOUR) * 4
    
    def fives(self):
        FIVE = 5
        return self.dice.count(FIVE) * 5
    
    def sixes(self):
        SIX = 6
        return self.dice.count(SIX) * 6
    
    @staticmethod
    def score_pair(*dice):
        for number in range(6, 0, -1):
            if dice.count(number) >= 2:
                return number * 2
        return 0

    @staticmethod
    def two_pairs(*dice):
        pairs = 0
        puntos = 0
        number = 1
        while pairs < 2 and number <= 6:
            if dice.count(number) >= 2:
                pairs += 1
                puntos += number * 2
            number += 1
        if pairs == 2:
            return puntos
        return 0
    
    @staticmethod
    def three_of_kind(*dice):
        for number in range(6, 0, -1):
            if dice.count(number) >= 3:
                return number * 3
        return 0
    
    @staticmethod
    def four_of_kind(*dice):
        for number in range(6, 0, -1):
            if dice.count(number) >= 4:
                return number * 4
        return 0
    
    @staticmethod
    def small_straight(*dice):
        for number in range(1, 6):
            if dice.count(number) != 1:
                return 0
        return Yatzy.chance(*dice)
    
    @staticmethod
    def large_straight(*dice):
        for number in range(2, 7):
            if dice.count(number) != 1:
                return 0
        return Yatzy.chance(*dice)

    @staticmethod
    def two_of_kind(*dice):
        for number in range(6, 0, -1):
            if dice.count(number) == 2:
                return number * 2
        return 0

    @staticmethod
    def full_house(*dice):
        if Yatzy.two_of_kind(*dice) and Yatzy.three_of_kind(*dice):
            return Yatzy.two_of_kind(*dice) + Yatzy.three_of_kind(*dice)
        return 0