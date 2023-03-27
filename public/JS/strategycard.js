const rows = ["Hands","8","9", "10", "11", "12", "13", "14","15", "16", "17", "2,2", "3,3", "4,4", "5,5", "6,6", "7,7", "8,8", "9,9", "10,10", "A,A", "A,2", "A,3", "A,4", "A,5","A,6", "A,7", "A,8", "A,9", "A,10"]  
  // read in strategy card
var strategy_card = []

function readCsv(){
    fetch('http://localhost:3000/strategy.csv')
    .then(response => response.json())
    .then(content => {
        content.forEach(item => {
            strategy_card.push(item)
        })
    });
}
/* returns the column for the dealer's card */
function dealerColumn(card){
    return strategy_card[0].indexOf(card)
}
/* returns the row for the player's hand */
function playerCardRow(cards, total){ 
    
    card1 = cards[0][0]
    card2 = cards[1][0]
    if (cards[0].legnth == 3 || cards[0][0] == "J"|| cards[0][0] == "Q"|| cards[0][0] == "K"){
        card1 = "10"
    }
    if (cards[1].legnth == 3 || cards[1][0] == "J"|| cards[1][0] == "Q"|| cards[1][0] == "K"){
        card2 = "10"
    }
    hand = card1 + "," + card2
    handswitch = card2 + "," + card1
    if ((rows.indexOf(hand) == -1 && rows.indexOf(handswitch) == -1) || cards.length > 2){
        return rows.indexOf(String(total))
    }
    
    if (rows.indexOf(handswitch) == -1)
        return rows.indexOf(hand)
    return rows.indexOf(handswtich)
}

/*Gets the best decision message accepting array of players cards, total of the cards added up, dealer's first card as a string*/ 
function getMessage(player, total, dealer){
    decision = strategy_card[playerCardRow(player,total)][dealerColumn(dealer)]
    if (decision == "H"){
        return "You should Hit"
    }
    else if (decision == "P"){
        return "You should Split"
    }
    else if (decision == "S"){
        return "You should Stand"
    }
    return "You should Double Down"
}