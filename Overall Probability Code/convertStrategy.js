const rows = ["Hands","8","9", "10", "11", "12", "13", "14","15", "16", "17", "2,2", "3,3", "4,4", "5,5", "6,6", "7,7", "8,8", "9,9", "10,10", "A,A", "A,2", "A,3", "A,4", "A,5","A,6", "A,7", "A,8", "A,9", "A,10"]  
// read in strategy card
  strategy_card = []
function readCsv(){

  /*const fs = require('fs')
  const content = fs.readFileSync('Blackjack Strategy Table.csv', 'utf-8')
  
  content.split("\r\n").forEach((line) => {
      if (line.split(",").length > 11){
        array = line.split(",")
        var newarray = []
        var letter1= array[0][1]
        var letter2= array[1][0]
        if (array[0].length > 2){
            letter1 = array[0][1] + array[0][2]
        }
        if (array[1].length > 2){
            letter2 = array[1][0] + array[1][1]
        }
        newarray.push(letter1+","+letter2)
        startlength = letter2.length+ letter1.length
        if (letter1.length == 2)
            startlength-=1
            if (letter2.length == 2)
            startlength-=1
        for(let i = startlength; i < array.length; i++){
            newarray.push(array[i])
        }
        strategy_card.push(newarray)
      } else {
        strategy_card.push(line.split(","))
      }
  });*/
  fetch('Blackjack Strategy Table.csv')
  .then(response => response.text())
  .then(content => {
    content.split("\r\n").forEach((line) => {
        if (line.split(",").length > 11){
          array = line.split(",")
          var newarray = []
          var letter1= array[0][1]
          var letter2= array[1][0]
          if (array[0].length > 2){
              letter1 = array[0][1] + array[0][2]
          }
          if (array[1].length > 2){
              letter2 = array[1][0] + array[1][1]
          }
          newarray.push(letter1+","+letter2)
          startlength = letter2.length+ letter1.length
          if (letter1.length == 2)
              startlength-=1
              if (letter2.length == 2)
              startlength-=1
          for(let i = startlength; i < array.length; i++){
              newarray.push(array[i])
          }
          strategy_card.push(newarray)
        } else {
          strategy_card.push(line.split(","))
        }
    });
  })
  .catch(error => console.error(error));

    // Remove the empty last row 
    strategy_card.pop()
    console.log(strategy_card)
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

/*number representation of card*//*
function convertCard(card){
    var val = 0
    if (card[0] == 'K' || card[0] == 'Q' || card[0] == 'J' || card.length == 3){
      val = 10;
    }
    else if (card[0] == 'A'){
      val = 11;
    }
    else {
      val = card[0]
    }
    return parseInt(val)
} 
var total = 0
for(let i = 0; i< player.length; i++){
    total+= convertCard(player[i])
}
decRep = strategy_card[playerCardRow(player,total)][dealerColumn(dealer)]
decision = ""
if (decRep == "H"){
 decsion = "Hit"
}
else if (decRep == "P"){
    decsion = "Split"
}
else if (decRep == "S"){
    decsion = "Stand"
}
else {
    decsion = "Double Down"
}

*/
readCsv()