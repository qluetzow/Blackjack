# Blackjack Copyright (C) 2019-2024 Quinn Luetzow
# This file is part of Standard Fantasy Character Generator.

# Blackjack is free software: you can
# redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.

# Blackjack is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See
# the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Blackjack. If not, see
# <https://www.gnu.org/licenses/>.

#!/usr/bin/env python3

"""Blackjack simulator.

Usage: python blackjack.py
"""

__author__ = "Quinn Luetzow"
__version__ = 0.1


from random import shuffle


class Card:
    def __init__(self, suit, value):
        self.self = self
        self.suit = suit
        self.value = value


class Shoe:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, deck_count=1):
        self.self = self
        self.deck_count = deck_count
        self.shoe = []
        self.shuffle()

    def shuffle(self):
        self.shoe = []
        for i in range(0, self.deck_count):
            for j in Shoe.suits:
                for k in Shoe.values:
                    self.shoe.append(Card([j], [k]))
        shuffle(self.shoe)

    def pull_card(self):
        try:
            return self.shoe.pop()
        except IndexError:
            print("Out of cards - must reshuffle.")



if __name__ == "__main__":
    exit(0)
