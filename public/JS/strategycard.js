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
    if (card.length == 3 || card[0] == "J"|| card[0] == "Q"|| card[0] == "K"){
        return strategy_card[0].indexOf(String(10))
    }
    return strategy_card[0].indexOf(String(card[0]))
}
/* returns the row for the player's hand */
function playerCardRow(cards, total){ 
    ret = ""
    if (cards.length == 2){
        if (cards[0][0] == cards [1][0]){
            if (cards[1].length > 2 || cards[1] == 'K' || cards[1] == 'Q' || cards[1] == 'J'){
                return 19
            }
            else if (cards[0][0]== 'A'){
                return 20
            }
            else {
                return 9 + parseInt(cards[1][0])
            }
        }
        if (cards[0][0] == 'A'){
            if (cards[1].length > 2 || cards[1] == 'K' || cards[1] == 'Q' || cards[1] == 'J'){
                return 29
            }
            else {
                return 19 + parseInt(cards[1][0])
            }
        } else if (cards[1][0] == 'A') {
            if (cards[0].length > 2 || cards[0] == 'K' || cards[0] == 'Q' || cards[0] == 'J'){
                return 29
            }
            else {
                return 19 + parseInt(cards[0][0])
            }
        }
    }
    if (total >= 17) {
        ret = rows.indexOf(String(17))
    } else if (total <=8){
        ret = rows.indexOf(String(8))
    } else {
        ret = rows.indexOf(String(total))
    }
    return ret
}

/*Gets the best decision message accepting array of players cards, total of the cards added up, dealer's first card as a string*/ 
function getMessage(player, total, dealer){
    var decision = strategy_card[playerCardRow(player, total)][dealerColumn(dealer[1])]
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