import random as rand
num = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suit = ["D", "S", "H", "C"]
deck = []
n = int(input("How many decks would you like to use (1, 2, 4, 6, or 8)"))
# create n decks
for decks in range(n):
  # create 1 deck
  for s in suit: 
    for n in num: 
      deck.append(n + s)

# shuffle deck
rand.shuffle(deck)
deck_original = deck.copy()
all_hands = []

# N hands
for i in range(1000000):
  hands = []
  for j in range(20):
    # When at 40% of deck is used reshuffle 
    if (len(deck) <= .4 * len(deck_original)):
      deck = deck_original.copy()
      rand.shuffle(deck)
    
    # Deal out card
    if (len(deck) != 0):
      hands.append(deck.pop(0))
  # add hands to list of file of hands
  all_hands.append(hands)
# make file of hands
with open("fileofmillionhands.txt", "w") as txt_file:
    for line in all_hands:
        txt_file.write(" ".join(line) + "\n") # works with any number of elements in a line
         
      
