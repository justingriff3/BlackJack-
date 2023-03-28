# BlackJack-Jackspot Enterprise



See deployed app here: https://black-jack-classic.vercel.app

<img width="1124" alt="blackjack" src="https://user-images.githubusercontent.com/39435918/53032256-1eba9980-3434-11e9-9367-28f3679426f7.PNG">

## Game Rules

1)  Object of the Game The participant attemptss to beat the dealer by getting a count as close     to 21 as possile, without going over 21

2)  It is up to user if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip     value.

3)  Before the game begins, each player places a bet in chips.

4)  

## Unique Game Features

#### Insurance

If the dealer shows an ace the player has the option to buy insurance. Insurance pays 2:1 if the dealer has a natural Blackjack

#### Dynamically Split Up to 5 Times

If the player has 2 cards of the same value, he may split his hand into two separate hands.

This makes coding the entire game about 2.5 times harder because an array of hand Objects must be used to keep track of all the player different split hands properties including position on the board.

Most online Blackjack games that allow splitting will hardcode the option to split 1 time.

## Known Bugs

Stack for insurance is not removed if player loses.
Split option sometimes does not show after standing with multiple split hands.


## Third Party Contributions

### Fonts
https://www.fontsquirrel.com/fonts/list/find_fonts?q%5Bterm%5D=chela&q%5Bsearch_check%5D=Y

### Images
Chip images made with Paint 3D

Bicycle Playing Cards

Buttons created with https://dabuttonfactory.com/
