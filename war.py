#!/usr/bin/python3

from random import shuffle
import os
os.system('clear')


#creating deck
suits = ['♣','♦','♥','♠',]
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

class Deck():
	'''52 cards, shuffle and split on half(26)'''
	def __init__(self):
		self.allcards = [(s,r) for s in suits for r in ranks]

	def shuffle(self):
		shuffle(self.allcards)

	def splitCards(self):
		return (self.allcards[:26],self.allcards[26:])

class Hand():
	'''Each player has a hand and can add or remove cards from hand'''
	def __init__(self, cards):
		self.cards = cards

	def __str__(self):
		return "Contains {} cards".format(len(self.cards))

	def add(self, added_сards):
		self.cards.extend(added_сards)

	def remove_card(self):
		return self.cards.pop()


class Player():
	'''Player playing'''
	def __init__(self,name,hand):
		self.name = name
		self.hand = hand

	def play_card(self):
		drawn_card = self.hand.remove_card()
		print("{} has placed: {}".format(self.name, drawn_card))
		return drawn_card

	def remove_war_cards(self):
		war_cards = []
		if len(self.hand.cards) < 3:
			return self.hand.cards
		else:
			for x in range(3):
				war_cards.append(self.hand.cards.pop())
			return war_cards

	def still_has_cards(self):
		'''Returns True if player still has cards'''
		return len(self.hand.cards) != 0

#GAME PLAY
print('##### WELCOME TO WAR CARD GAME #####')

#CREATING NEW DECK AND SPLITING IT
deck = Deck()
deck.shuffle()
half1,half2 = deck.splitCards()

#CREATE BOTH PLAYERS
comp = Player("Computer",Hand(half1))

name = input('\nWhat is your name? ')
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
	total_rounds += 1
	print("\nTime for new round!")
	print("Here are the current standings")
	print(user.name +" has the count: "+str(len(user.hand.cards)))
	print(comp.name +" has the count: "+str(len(comp.hand.cards)))
	print("Play a card!")
	print("\n")

	table_cards = []
	c_card = comp.play_card()
	p_card = user.play_card()
	input("Press to continue")

	table_cards.append(c_card)
	table_cards.append(p_card)

	if c_card[1] == p_card[1]:
		war_count += 1
		print("WAR!!!")

		table_cards.extend(user.remove_war_cards())
		table_cards.extend(comp.remove_war_cards())

		if ranks.index(c_card[1]) < ranks.index(p_card[1]):
			user.hand.add(table_cards)
		else:
			comp.hand.add(table_cards)

	else:
		if ranks.index(c_card[1]) < ranks.index(p_card[1]):
			user.hand.add(table_cards)
		else:
			comp.hand.add(table_cards)

print("GAME OVER, NUMBER OF ROUNDS: "+str(total_rounds))
print("WAR HAPPEN "+str(war_count)+" times")