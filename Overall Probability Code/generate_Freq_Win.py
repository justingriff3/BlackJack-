import pandas as pd
import random as rand

#*************************************************************************FREQUENCY****************************************************************************************************************************************************************
freq_nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nums = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
freq_hands = ["8","9", "10", "11", "12", "13", "14","15", "16", "17", "2,2", "3,3", "4,4", "5,5", "6,6", "7,7", "8,8", "9,9", "10,10", "A,A", "A,2", "A,3", "A,4", "A,5","A,6", "A,7", "A,8", "A,9", "A,10"]

# Create Frequency Table
freq_df = pd.DataFrame({"Hands":freq_hands.copy(),"2":freq_nums.copy(), "3":freq_nums.copy(), "4": freq_nums.copy(), "5":freq_nums.copy(), "6":freq_nums.copy(), "7":freq_nums.copy(), "8":freq_nums.copy(), "9":freq_nums.copy(), "10":freq_nums.copy(), "A":freq_nums.copy()})
# Add Double Hand Scenario to Frequency Table
def addDouble(player, dealer):
  row = 0
  if player[0][0] == 'J'or player[0][0] == 'Q' or player[0][0] == 'K' or len(player[0]) > 2:
    row = 8+ 10
  elif player [0][0] == 'A':
    row = 8 + 11
  else: 
    row = 8 + int(player[0][0])
  
  if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
     freq_df.at[row, str(10)] = int (freq_df.iloc[row][str(10)]) + 1
  else:
    freq_df.at[row, dealer[0][0]] = freq_df.iloc[row][dealer[0][0]] + 1 
# Add Ace Hand Scenario to Frequency Table
def addAceHand(player, dealer):
  row = 0
  if (player[0][0] == "A"):
    if player[1][0] == 'J'or player[1][0] == 'Q' or player[1][0] == 'K' or len(player[1]) > 2:
      row = 10 + 18
    else:
      row = int(player [1][0]) +18
    if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
      freq_df.at[row, str(10)] = int (freq_df.iloc[row][str(10)]) + 1
    else:
        freq_df.at[row, dealer[0][0]] = freq_df.iloc[row][dealer[0][0]] +1
  else: 
    if player[0][0] == 'J'or player[0][0] == 'Q' or player[0][0] == 'K' or len(player[0]) > 2:
      row = 10 + 18
    else:
      row = int(player [0][0]) +18
    if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
      freq_df.at[row, str(10)] = int (freq_df.iloc[row][str(10)]) + 1
    else:
        freq_df.at[row, dealer[0][0]] = freq_df.iloc[row][dealer[0][0]] +1

# Add Pair that are not the same to the Frequency Table
def add(dealer, total):
  row = total - 8
  if total >= 17:
    row = 17 -8
  if row < 0 :
    if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
      freq_df.at[0, str(10) ] = freq_df.iloc[0][str(10)] + 1
    else:
      freq_df.at[0, dealer[0][0]] = freq_df.iloc[0][dealer[0][0]] + 1
  else:
    if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
      freq_df.at[ row, str(10) ] = freq_df.iloc[row][str(10)] + 1
    else:
      freq_df.at[row, dealer[0][0]] = freq_df.iloc[row][dealer[0][0]] + 1

# Standard Frequency Method
def addToFreq (player, dealer, total):
  if player[0][0] == player[1][0]:
    addDouble(player, dealer)
  elif player[0][0] == 'A' or player[1][0] == 'A':
    addAceHand(player, dealer)
  else: 
    add(dealer, total)
    
    
#************************************************************************SPLIT WINNING****************************************************************************************************************************************************************

# Create Winability Split Table
win_split_df = pd.DataFrame({"Hands":freq_hands.copy(),"2":nums.copy(), "3":nums.copy(), "4": nums.copy(), "5":nums.copy(), "6":nums.copy(), "7":nums.copy(), "8":nums.copy(), "9":nums.copy(), "10":nums.copy(), "A":nums.copy()})
def addToSplitWin(dealer,player,result):
  row = 0
  if player[0][0] == 'J'or player[0][0] == 'Q' or player[0][0] == 'K' or len(player[0]) > 2:
    row = 8+ 10
  elif player [0][0] == 'A':
    row = 8 + 11
  else: 
    row = 8 + int(player[0][0])
  if ("Win" in result or "Loss" in result or "Bust" in result):
    if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2 :
      if (result [0] == "Win"):
        win_split_df.at[row,str(10)] += .5
      if (result [1] == "Win"):
        win_split_df.at[row,str(10)] += .5
    else:
        if (result [0] == "Win"):
          win_split_df.at[row,dealer[0][0]] += .5
        if (result [1] == "Win"):
          win_split_df.at[row,dealer[0][0]] += .5    
#************************************************************************HIT WINNING****************************************************************************************************************************************************************
# Create Winability Hit Table
win_hit_df = pd.DataFrame({"Hands":freq_hands.copy(),"2":nums.copy(), "3":nums.copy(), "4": nums.copy(), "5":nums.copy(), "6":nums.copy(), "7":nums.copy(), "8":nums.copy(), "9":nums.copy(), "10":nums.copy(), "A":nums.copy()})
def addDoubleHit(dealer,player,result):
  row = 0
  if player[0][0] == 'J'or player[0][0] == 'Q' or player[0][0] == 'K' or len(player[0]) > 2:
    row = 8+ 10
  elif player [0][0] == 'A' or player [1][0] == 'A':
    row = 8 + 11
  else: 
    row = 8 + int(player[0][0])
  if  "Win" in result or "Loss" in result or "Bust" in result  :
    if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2 :
      if (result [0] == "Win"):
        win_hit_df.at[row,str(10)] +=1
    else:
      if (result [0] == "Win"):
        win_hit_df.at[row, dealer[0][0]] += 1

def addAceHandHit(player, dealer, result):
  row = 0
  if "Win" in result or "Loss" in result or "Bust" in result: 
    if (player[0][0] == "A"):
      if player[1][0] == 'J'or player[1][0] == 'Q' or player[1][0] == 'K' or len(player[1]) > 2:
        row = 10 + 18
      else:
        row = int(player [1][0]) +18
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_hit_df.at[row, str(10)]+=1
      else:
        if (result [0] == "Win"):
          win_hit_df.at[row, dealer[0][0]]+=1
    else: 
      if player[0][0] == 'J'or player[0][0] == 'Q' or player[0][0] == 'K' or len(player[0]) > 2:
        row = 10 + 18
      else:
        row = int(player [0][0]) +18
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_hit_df.at[row, str(10)]+=1
      else:
        if (result [0] == "Win"):
          win_hit_df.at[row, dealer[0][0]] +=1
           
def addHit(dealer, total, result):
  row = total - 8
  if total >= 17:
    row = 17 -8
  if "Win" in result or "Loss" in result or "Bust" in result:
    if row < 0 :
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_hit_df.at[0, str(10)]+=1
        
      else:
        if (result [0] == "Win"):
          win_hit_df.at[0, dealer[0][0]]+=1
    else:
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_hit_df.at [row, str(10)]+=1
      else:
        if (result [0] == "Win"):
          win_hit_df.at[row, dealer[0][0]]+=1
        
def addToHitWin(dealer,player,result, total):
  if player[1][0] == player[0][0]:
    addDoubleHit(dealer, player, result)
  elif player[0][0] == 'A' or player[1][0] == 'A':
    addAceHandHit(player, dealer, result)
  else: 
    addHit(dealer, total, result)

#************************************************************************STAND WINNING****************************************************************************************************************************************************************

# Create Winability Stand Table
win_stand_df = pd.DataFrame({"Hands":freq_hands.copy(),"2":nums.copy(), "3":nums.copy(), "4": nums.copy(), "5":nums.copy(), "6":nums.copy(), "7":nums.copy(), "8":nums.copy(), "9":nums.copy(), "10":nums.copy(), "A":nums.copy()})

def addDoubleStand(dealer,player,result):
  row = 0
  if player[0][0] == 'J'or player[0][0] == 'Q' or player[0][0] == 'K' or len(player[0]) > 2:
    row = 8+ 10
  elif player [0][0] == 'A':
    row = 8 + 11
  else: 
    row = 8 + int(player[0][0])
  if "Win" in result or "Loss" in result or "Bust" in result:
    if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2 :
      if (result [0] == "Win"):
        win_stand_df.at[row, str(10)]+=1  
    else:
      if (result [0] == "Win"):
        win_stand_df.at[row, dealer[0][0]]+=1
      
def addAceHandStand(player, dealer, result):
  row = 0
  if "Win" in result or "Loss" in result or "Bust" in result: 
    if (player[0][0] == "A"):
      if player[1][0] == 'J'or player[1][0] == 'Q' or player[1][0] == 'K' or len(player[1]) > 2:
        row = 10 + 18
      else:
        row = int(player [1][0]) +18
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_stand_df.at[row, str(10)]+=1
      else:
        if (result [0] == "Win"):
          win_stand_df.at[row, dealer[0][0]]+=1
    else: 
      if player[0][0] == 'J'or player[0][0] == 'Q' or player[0][0] == 'K' or len(player[0]) > 2:
        row = 10 + 18
      else:
        row = int(player [0][0]) +18
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_stand_df.at[row, str(10)]+=1
      else:
        if (result [0] == "Win"):
          win_stand_df.at[row, dealer[0][0]]+=1
def addStand(dealer, total, result):
  row = total - 8
  if total >= 17:
    row = 17 -8
  if "Win" in result or "Loss" in result or "Bust" in result:
    if row < 0 :
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_stand_df.at[0, str(10)]+=1
      else:
        if (result [0] == "Win"):
          win_stand_df.at[0, dealer[0][0]]+=1
    else:
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_stand_df.at[row, str(10)]+=1
      else:
        if (result [0] == "Win"):
          win_stand_df.at[row, dealer[0][0]]+=1

def addToStandWin(dealer,player,result, total):
  if player[0][0] == player[1][0]:
    addDoubleStand(dealer, player, result)
  elif player[0][0] == 'A' or player[1][0] == 'A':
    addAceHandStand(player, dealer, result)
  else: 
    addStand(dealer, total, result)
   
#************************************************************************DOUBLE DOWN WINNING****************************************************************************************************************************************************************

# Create Winability Double Down Table
win_dd_df = pd.DataFrame({"Hands":freq_hands.copy(),"2":nums.copy(), "3":nums.copy(), "4": nums.copy(), "5":nums.copy(), "6":nums.copy(), "7":nums.copy(), "8":nums.copy(), "9":nums.copy(), "10":nums.copy(), "A":nums.copy()})

def addDoubleDD(dealer,player,result):
  row = 0
  if player[0][0] == 'J'or player[0][0] == 'Q' or player[0][0] == 'K' or len(player[0]) > 2:
    row = 8+ 10
  elif player [0][0] == 'A':
    row = 8 + 11
  else: 
    row = 8 + int(player[0][0])
  if "Win" in result or "Loss" in result or "Bust" in result:
    if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2 :
      if (result [0] == "Win"):
        win_dd_df.at[row, str(10)]+=1
    else:
      if (result[0] == "Win"):
        if (result [0] == "Win"):
          win_dd_df.at[row, dealer[0][0]]+=1
def addAceHandDD(player, dealer, result):
  row = 0
  if "Win" in result or "Loss" in result or "Bust" in result: 
    if (player[0][0] == "A"):
      if player[1][0] == 'J'or player[1][0] == 'Q' or player[1][0] == 'K' or len(player[1]) > 2:
        row = 10 + 18
      else:
        row = int(player [1][0]) +18
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_dd_df.at[row, str(10)]+=1
      else:
        if (result [0] == "Win"):
          win_dd_df.at[row, dealer[0][0]]+=1
    else: 
      if player[0][0] == 'J'or player[0][0] == 'Q' or player[0][0] == 'K' or len(player[0]) > 2:
        row = 10 + 18
      else:
        row = int(player [0][0]) +18
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_dd_df.at[row, str(10)]+=1
      else:
        if (result [0] == "Win"):
          win_dd_df.at[row,dealer[0][0]]+=1
def addDD(dealer, total, result):
  row = total - 8
  if total >= 17:
    row = 17 -8
  if "Win" in result or "Loss" in result or "Bust" in result:
    if row < 0 :
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_dd_df.at[0, str(10)]+=1
      else:
        if (result [0] == "Win"):
          win_dd_df.at[0, dealer[0][0]]+=1
    else:
      if dealer[0][0] == 'J'or dealer[0][0] == 'Q' or dealer[0][0] == 'K' or len(dealer[0]) > 2:
        if (result [0] == "Win"):
          win_dd_df.at [row, str(10)]+=1
      else:
        if (result [0] == "Win"):
          win_dd_df.at[row, dealer[0][0]]+=1

def addToDDWin(dealer,player,result, total):
  if player[0][0] == player[1][0]:
    addDoubleDD(dealer, player, result)
  elif player[0][0] == 'A' or player[1][0] == 'A':
    addAceHandDD(player, dealer, result)
  else: 
    addDD(dealer, total, result)
#************************************************************************STRATEGY TABLE****************************************************************************************************************************************************************
emptystr = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]

strategy_table = pd.DataFrame({"Hands":freq_hands.copy(),"2":emptystr.copy(), "3":emptystr.copy(), "4": emptystr.copy(), "5":emptystr.copy(), "6":emptystr.copy(), "7":emptystr.copy(), "8":emptystr.copy(), "9":emptystr.copy(), "10":emptystr.copy(), "A":emptystr.copy()})
winning_strategy_table = pd.DataFrame({"Hands":freq_hands.copy(),"2":nums.copy(), "3":nums.copy(), "4": nums.copy(), "5":nums.copy(), "6":nums.copy(), "7":nums.copy(), "8":nums.copy(), "9":nums.copy(), "10":nums.copy(), "A":nums.copy()})
probability_strategy_table = win_dd_df = pd.DataFrame({"Hands":freq_hands.copy(),"2":nums.copy(), "3":nums.copy(), "4": nums.copy(), "5":nums.copy(), "6":nums.copy(), "7":nums.copy(), "8":nums.copy(), "9":nums.copy(), "10":nums.copy(), "A":nums.copy()})
 
dealer_hand = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A"]
def draftStrategyTable():
   for row in range(0,29):
      for col in dealer_hand:
         frequency = int(freq_df.iloc[row][col])
         win_split = win_split_df.iloc[row][col]
         win_stand = win_stand_df.iloc[row][col]
         win_hit = win_hit_df.iloc[row][col]
         win_dd = win_dd_df.iloc[row][col]
         # Double Down is the bets option 
         a = ((win_dd/frequency)* frequency, (win_stand/frequency)* frequency, (win_split/frequency)* frequency, (win_hit/frequency)* frequency)
         l_max = max(a)
         if (win_dd/frequency)* frequency == l_max:
            strategy_table.at[row, col] = "D"
            winning_strategy_table.at[row,col] = win_dd
            probability_strategy_table.at[row,col] = (win_dd/frequency)
         elif (win_stand/frequency)* frequency == l_max:
            strategy_table.at[row, col] = "S"
            winning_strategy_table.at[row,col] = win_stand
            probability_strategy_table.at[row,col] = (win_stand/frequency)
         elif (win_split/frequency)* frequency == l_max:
            strategy_table.at[row, col] = "P"
            winning_strategy_table.at[row,col] = win_split
            probability_strategy_table.at[row,col] = (win_split/frequency)
         elif (win_hit/frequency)* frequency == l_max:
            strategy_table.at[row, col] = "H"
            winning_strategy_table.at[row,col] = win_hit
            probability_strategy_table.at[row,col] = (win_hit/frequency)
           

#************************************************************************DOUBLE DOWN SCENARIO****************************************************************************************************************************************************************

# Double Down (D)
def DoubleDown(cards):
  aces = []
  hand = [cards[0], cards[2]]
  if hand [0][0] == 'A':
    aces.append(hand[0])
  
  if hand [1][0] == 'A':
    aces.append(hand[1])
    
  total = convertCard(hand[0]) + convertCard(hand[1])
  action = ["Card"]
  next_card = 5
  hand.append(cards[4])
  if cards[4][0] == 'A':
    aces.append(cards[4])
  total += convertCard(hand[2])
  if total > 21 and len(aces) != 0:
    aces.pop(0)
    total-=10
  
  dealer_aces = [] 
  if cards[1][0] == 'A':
   dealer_aces.append(cards[1])
  if cards[0][0] == 'A':
   dealer_aces.append(cards[0])
  dealer_hand = [cards[1], cards[3]]
  dealertotal = convertCard(dealer_hand[0]) + convertCard(dealer_hand[1])
  
  while dealertotal < 17 and total <= 21:
    dealer_hand.append(cards[next_card])
    dealertotal+= convertCard(cards[next_card])
    if cards[next_card][0] == 'A':
       dealer_aces.append(cards[next_card][0])
    next_card+=1
    if dealertotal > 21 and len(dealer_aces) != 0:
      dealertotal -=10
      dealer_aces.pop(0)

  results = []
  # win, lose or draw
  if total > 21:
    results.append("Bust")
  elif total < dealertotal and dealertotal <= 21:
    results.append("Loss")
  elif dealertotal > 21:
    results.append("Win")
  elif dealertotal < total and total <= 21:
    results.append("Win")
  else:
    results.append("Draw")
  Dealer = ["-", "-", cards[1], "-", cards[3]]
  hand.pop(0)
  hand.pop(0)
  Player = ["Hand", cards[0], "-", cards[2], "-"]
  dealer_hand.pop(0)
  dealer_hand.pop(0)
  Action = ["Action", "-", "-", "Double Down", " "]
  for i in range(len(options)-3):
    if len(hand) != 0:
      Player.append(hand.pop(0))
      Dealer.append(" ")
      Action.append(action.pop(0))
    elif len(dealer_hand) != 0 and len(hand) == 0:
      Player.append("-")
      Dealer.append(dealer_hand.pop(0))
      Action.append("-")
    else:
      Player.append("-")
      Dealer.append("-")
      Action.append("-")
  Player.append(str(total))
  Dealer.append(str(dealertotal))
  Action.append(" ")

  Player.append(results[0])
  Dealer.append("-")
  Action.append("-")
  addToDDWin([cards[1], cards[3]],[cards[0], cards[2]], results, convertCard(cards[0])+convertCard(cards[2]))

  return {'Dealer'+str(scenarioInt): Dealer, 'Player'+str(scenarioInt): Player, "Act"+ str(scenarioInt):Action}
  
#************************************************************************HIT SCENARIO****************************************************************************************************************************************************************

# Hit (H)
def Hit(cards):
  aces = []
  hand = [cards[0], cards[2]]
  total = convertCard(cards[0]) + convertCard(cards[2])
  action = []
  next_card = 4
  if cards [0][0] == 'A':
    aces.append(cards[0])
  if cards [2][0] == 'A':
    aces.append(cards[2])
  if total > 21 and len(aces) != 0:
   aces.pop(0)
   total -=10
  #hit hand
  while(total <= 17):
      action.append("Hit")
      hand.append(cards[next_card])
      total+= convertCard(cards[next_card])
      if(cards[next_card] [0] == "A"):
        aces.append(cards[next_card])
      next_card+=1
      if total > 21 and len(aces) != 0:
        aces.pop(0)
        total -=10
  dealer_aces = [] 
  if cards[1][0] == 'A':
   dealer_aces.append(cards[1])
  if cards[0][0] == 'A':
   dealer_aces.append(cards[0])
  dealer_hand = [cards[1], cards[3]]
  dealertotal = convertCard(dealer_hand[0]) + convertCard(dealer_hand[1])
  
  while dealertotal < 17 and total <= 21:
    dealer_hand.append(cards[next_card])
    dealertotal+= convertCard(cards[next_card])
    if cards[next_card][0] == 'A':
       dealer_aces.append(cards[next_card][0])
    next_card+=1
    if dealertotal > 21 and len(dealer_aces) != 0:
      dealertotal -=10
      dealer_aces.pop(0)

  results = []
  # win, lose or draw
  if total > 21:
    results.append("Bust")
  elif total < dealertotal and dealertotal <= 21:
    results.append("Loss")
  elif dealertotal > 21:
    results.append("Win")
  elif dealertotal < total and total <= 21:
    results.append("Win")
  else:
    results.append("Draw")
  Dealer = ["-", "-", cards[1], "-", cards[3]]
  hand.pop(0)
  hand.pop(0)
  Player = ["Hand", cards[0], "-", cards[2], "-"]
  dealer_hand.pop(0)
  dealer_hand.pop(0)
  Action = ["Action", "-", "-", "Hit", " "]
  for i in range(len(options)-3):
    if len(hand) != 0:
      Player.append(hand.pop(0))
      Dealer.append("-")
      Action.append(action.pop(0))
    elif len(dealer_hand) != 0 and len(hand) == 0:
      Player.append("-")
      Dealer.append(dealer_hand.pop(0))
      Action.append("-")
    else:
      Player.append("-")
      Dealer.append("-")
      Action.append("-")
  Player.append(str(total))
  Dealer.append(str(dealertotal))
  Action.append(" ")

  Player.append(results[0])
  Dealer.append("-")
  Action.append("-")
  addToHitWin([cards[1], cards[3]],[cards[0], cards[2]],results, convertCard(cards[0])+convertCard(cards[2]))
  return {'Dealer'+str(scenarioInt): Dealer, 'Player'+str(scenarioInt): Player, "Act"+ str(scenarioInt):Action}
  
#************************************************************************SPLIT SCENARIO****************************************************************************************************************************************************************

# Split (P)
def SplitHit(cards):
  aces1 = []
  hand1 = [cards[0]]
  hand1_act = []
  aces2 = []
  hand2 = [cards[2]]
  hand2_act = []
  total1 = convertCard(cards[0])
  next_card = 4
  if hand1 [0][0] == 'A':
    aces1.append(hand1[0])
  elif hand2 [0][0] == 'A':
    aces2.append(hand2[0])
  #hand1
  while(total1 < 17):
      hand1_act.append("Hit")
      hand1.append(cards[next_card])
      if cards[next_card] [0] == 'A':
        aces1.append(cards[next_card])
      total1+= convertCard(cards[next_card])
      next_card+=1
      if total1 > 21 and len(aces1) != 0:
        aces1.pop(0)
        total1 -= 10
  total2 = convertCard(cards[2])
  while(total2 < 17):
      hand2_act.append("Hit")
      hand2.append(cards[next_card])
      if cards[next_card ] [0] == 'A':
        aces2.append(cards[next_card])
      total2+= convertCard(cards[next_card])
      next_card+=1
      if total2 > 21 and len(aces2) != 0:
        aces2.pop(0)
        total2 -=10
  dealer_aces = [] 
  if cards[1][0] == 'A':
   dealer_aces.append(cards[1])
  if cards[0][0] == 'A':
   dealer_aces.append(cards[0])
  dealer_hand = [cards[1], cards[3]]
  dealertotal = convertCard(dealer_hand[0]) + convertCard(dealer_hand[1])
  
  while dealertotal < 17 and total <= 21:
    dealer_hand.append(cards[next_card])
    dealertotal+= convertCard(cards[next_card])
    if cards[next_card][0] == 'A':
       dealer_aces.append(cards[next_card][0])
    next_card+=1
    if dealertotal > 21 and len(dealer_aces) != 0:
      dealertotal -=10
      dealer_aces.pop(0)

  results = []
  # hand #1 
  if total1 > 21:
    results.append("Bust")
  elif total1 < dealertotal and dealertotal <= 21:
    results.append("Loss")
  elif dealertotal > 21:
    results.append("Win")
  elif dealertotal < total1 and total1 <= 21:
    results.append("Win")
  else:
    results.append("Draw")

  #hand  #2
  if total2 > 21:
    results.append("Bust")
  elif total2 < dealertotal and dealertotal <= 21:
    results.append("Loss")
  elif dealertotal > 21:
    results.append("Win")
  elif dealertotal < total2 and total2 <= 21:
    results.append("Win")
  else:
    results.append("Draw")
  dealer = [" ", " ", dealer_hand.pop(0), " ",dealer_hand.pop(0)]
  playhand1 = ["Hand 1", hand1.pop(0), " ", " ", " "]
  action1 = ["hand1_Action", " ", " ", "Split", " "]
  playhand2 = ["Hand 2", " ", " ", hand2.pop(0), " "]
  action2 = ["hand2_Action", " ", " ", " ", " "]
  for i in range(len(options)-3):
    if (len(hand1)!= 0):
      dealer.append("-")
      playhand1.append(hand1.pop(0))
      action1.append(hand1_act.pop(0))
      playhand2.append("-")
      action2.append("-")
    elif(len(hand2)!= 0):
      dealer.append("-")
      playhand1.append("-")
      action1.append("-")
      playhand2.append(hand2.pop(0))
      action2.append(hand2_act.pop(0))
    elif(len(dealer_hand) != 0):
      dealer.append(dealer_hand.pop(0))
      playhand1.append("-")
      action1.append("-")
      playhand2.append("-")
      action2.append("-")
    else:
      dealer.append("-")
      playhand1.append("-")
      action1.append("-")
      playhand2.append("-")
      action2.append("-")
  dealer.append(str(dealertotal))
  playhand1.append(str(total1))
  action1.append("- ")
  playhand2.append(str(total2))
  action2.append("-") 
  
  dealer.append(" ")
  playhand1.append(results[0])
  action1.append(" ")
  playhand2.append(results[1])
  action2.append(" ") 
   
  addToSplitWin([cards[1], cards[3]],[cards[0], cards[2]],results)
  return {"Dealer"+str(scenarioInt): dealer, "Player"+str(scenarioInt): playhand1, "Act1"+str(scenarioInt): action1, "P"+str(scenarioInt): playhand2, "Act2"+str(scenarioInt):action2}
def SplitStand(cards):
  aces1 = []
  hand1 = [cards[0]]
  hand1_act = []
  aces2 = []
  hand2 = [cards[2]]
  hand2_act = []
  total1 = convertCard(cards[0])
  next_card = 4
  if hand1 [0][0] == 'A':
    aces1.append(hand1[0])
  elif hand2 [0][0] == 'A':
    aces2.append(hand2[0])
  #hand1
  while(total1 < 17):
      hand1_act.append("Hit")
      hand1.append(cards[next_card])
      if cards[next_card] [0] == 'A':
        aces1.append(cards[next_card])
      total1+= convertCard(cards[next_card])
      next_card+=1
      if total1 > 21 and len(aces1) != 0:
        aces1.pop(0)
        total1 -= 10
  total2 = convertCard(cards[2])
  while(total2 < 17):
      hand2_act.append("Hit")
      hand2.append(cards[next_card])
      if cards[next_card ] [0] == 'A':
        aces2.append(cards[next_card])
      total2+= convertCard(cards[next_card])
      next_card+=1
      if total2 > 21 and len(aces2) != 0:
        aces2.pop(0)
        total2 -=10
  dealer_aces = [] 
  if cards[1][0] == 'A':
   dealer_aces.append(cards[1])
  if cards[0][0] == 'A':
   dealer_aces.append(cards[0])
  dealer_hand = [cards[1], cards[3]]
  dealertotal = convertCard(dealer_hand[0]) + convertCard(dealer_hand[1])
  
  while dealertotal < 17 and total <= 21:
    dealer_hand.append(cards[next_card])
    dealertotal+= convertCard(cards[next_card])
    if cards[next_card][0] == 'A':
       dealer_aces.append(cards[next_card][0])
    next_card+=1
    if dealertotal > 21 and len(dealer_aces) != 0:
      dealertotal -=10
      dealer_aces.pop(0)

  results = []
  # hand #1 
  if total1 > 21:
    results.append("Bust")
  elif total1 < dealertotal and dealertotal <= 21:
    results.append("Loss")
  elif dealertotal > 21:
    results.append("Win")
  elif dealertotal < total1 and total1 <= 21:
    results.append("Win")
  else:
    results.append("Draw")

  #hand  #2
  if total2 > 21:
    results.append("Bust")
  elif total2 < dealertotal and dealertotal <= 21:
    results.append("Loss")
  elif dealertotal > 21:
    results.append("Win")
  elif dealertotal < total2 and total2 <= 21:
    results.append("Win")
  else:
    results.append("Draw")
  dealer = [" ", " ", dealer_hand.pop(0), " ",dealer_hand.pop(0)]
  playhand1 = ["Hand 1", hand1.pop(0), " ", " ", " "]
  action1 = ["hand1_Action", " ", " ", "Split", " "]
  playhand2 = ["Hand 2", " ", " ", hand2.pop(0), " "]
  action2 = ["hand2_Action", " ", " ", " ", " "]
  for i in range(len(options)-3):
    if (len(hand1)!= 0):
      dealer.append("-")
      playhand1.append(hand1.pop(0))
      action1.append(hand1_act.pop(0))
      playhand2.append("-")
      action2.append("-")
    elif(len(hand2)!= 0):
      dealer.append("-")
      playhand1.append("-")
      action1.append("-")
      playhand2.append(hand2.pop(0))
      action2.append(hand2_act.pop(0))
    elif(len(dealer_hand) != 0):
      dealer.append(dealer_hand.pop(0))
      playhand1.append("-")
      action1.append("-")
      playhand2.append("-")
      action2.append("-")
    else:
      dealer.append("-")
      playhand1.append("-")
      action1.append("-")
      playhand2.append("-")
      action2.append("-")
  dealer.append(str(dealertotal))
  playhand1.append(str(total1))
  action1.append("- ")
  playhand2.append(str(total2))
  action2.append("-") 
  
  dealer.append(" ")
  playhand1.append(results[0])
  action1.append(" ")
  playhand2.append(results[1])
  action2.append(" ") 
   
  addToSplitWin([cards[1], cards[3]],[cards[0], cards[2]],results) 
   
   
def SplitDD(cards):
  aces1 = []
  hand1 = [cards[0]]
  hand1_act = []
  aces2 = []
  hand2 = [cards[2]]
  hand2_act = []
  total1 = convertCard(cards[0])
  next_card = 4
  if hand1 [0][0] == 'A':
    aces1.append(hand1[0])
  elif hand2 [0][0] == 'A':
    aces2.append(hand2[0])
  #hand1
  while(total1 < 17):
      hand1_act.append("Hit")
      hand1.append(cards[next_card])
      if cards[next_card] [0] == 'A':
        aces1.append(cards[next_card])
      total1+= convertCard(cards[next_card])
      next_card+=1
      if total1 > 21 and len(aces1) != 0:
        aces1.pop(0)
        total1 -= 10
  total2 = convertCard(cards[2])
  while(total2 < 17):
      hand2_act.append("Hit")
      hand2.append(cards[next_card])
      if cards[next_card ] [0] == 'A':
        aces2.append(cards[next_card])
      total2+= convertCard(cards[next_card])
      next_card+=1
      if total2 > 21 and len(aces2) != 0:
        aces2.pop(0)
        total2 -=10
  dealer_aces = [] 
  if cards[1][0] == 'A':
   dealer_aces.append(cards[1])
  if cards[0][0] == 'A':
   dealer_aces.append(cards[0])
  dealer_hand = [cards[1], cards[3]]
  dealertotal = convertCard(dealer_hand[0]) + convertCard(dealer_hand[1])
  
  while dealertotal < 17 and total <= 21:
    dealer_hand.append(cards[next_card])
    dealertotal+= convertCard(cards[next_card])
    if cards[next_card][0] == 'A':
       dealer_aces.append(cards[next_card][0])
    next_card+=1
    if dealertotal > 21 and len(dealer_aces) != 0:
      dealertotal -=10
      dealer_aces.pop(0)

  results = []
  # hand #1 
  if total1 > 21:
    results.append("Bust")
  elif total1 < dealertotal and dealertotal <= 21:
    results.append("Loss")
  elif dealertotal > 21:
    results.append("Win")
  elif dealertotal < total1 and total1 <= 21:
    results.append("Win")
  else:
    results.append("Draw")

  #hand  #2
  if total2 > 21:
    results.append("Bust")
  elif total2 < dealertotal and dealertotal <= 21:
    results.append("Loss")
  elif dealertotal > 21:
    results.append("Win")
  elif dealertotal < total2 and total2 <= 21:
    results.append("Win")
  else:
    results.append("Draw")
  dealer = [" ", " ", dealer_hand.pop(0), " ",dealer_hand.pop(0)]
  playhand1 = ["Hand 1", hand1.pop(0), " ", " ", " "]
  action1 = ["hand1_Action", " ", " ", "Split", " "]
  playhand2 = ["Hand 2", " ", " ", hand2.pop(0), " "]
  action2 = ["hand2_Action", " ", " ", " ", " "]
  for i in range(len(options)-3):
    if (len(hand1)!= 0):
      dealer.append("-")
      playhand1.append(hand1.pop(0))
      action1.append(hand1_act.pop(0))
      playhand2.append("-")
      action2.append("-")
    elif(len(hand2)!= 0):
      dealer.append("-")
      playhand1.append("-")
      action1.append("-")
      playhand2.append(hand2.pop(0))
      action2.append(hand2_act.pop(0))
    elif(len(dealer_hand) != 0):
      dealer.append(dealer_hand.pop(0))
      playhand1.append("-")
      action1.append("-")
      playhand2.append("-")
      action2.append("-")
    else:
      dealer.append("-")
      playhand1.append("-")
      action1.append("-")
      playhand2.append("-")
      action2.append("-")
  dealer.append(str(dealertotal))
  playhand1.append(str(total1))
  action1.append("- ")
  playhand2.append(str(total2))
  action2.append("-") 
  
  dealer.append(" ")
  playhand1.append(results[0])
  action1.append(" ")
  playhand2.append(results[1])
  action2.append(" ") 
   
  addToSplitWin([cards[1], cards[3]],[cards[0], cards[2]],results)
   
   
def Split(cards):
   return SplitHit(cards)
#************************************************************************STAND SCENARIO****************************************************************************************************************************************************************

# Stand (S)
def Stand(cards):
  aces = []
  hand = [cards[0], cards[2]]
  total = convertCard(hand[0]) + convertCard(hand[1])
  next_card = 4
  action = []
  if cards[0][0] == 'A':
   aces.append(cards[0])
  if cards[1][0] == 'A':
   aces.append(cards[1])
   
  if total > 21 and len(aces) != 0:
   aces.pop(0)
   total -=10
  dealer_hand = [cards[1], cards[3]]
  
  dealer_aces = [] 
  if cards[1][0] == 'A':
   dealer_aces.append(cards[1])
  if cards[0][0] == 'A':
   dealer_aces.append(cards[0])
  dealer_hand = [cards[1], cards[3]]
  dealertotal = convertCard(dealer_hand[0]) + convertCard(dealer_hand[1])
  
  while dealertotal < 17 and total <= 21:
    dealer_hand.append(cards[next_card])
    dealertotal+= convertCard(cards[next_card])
    if cards[next_card][0] == 'A':
       dealer_aces.append(cards[next_card][0])
    next_card+=1
    if dealertotal > 21 and len(dealer_aces) != 0:
      dealertotal -=10
      dealer_aces.pop(0)


  results = []
  # win, lose or draw
  if total > 21:
    results.append("Bust")
  elif total < dealertotal and dealertotal <= 21:
    results.append("Loss")
  elif dealertotal > 21:
    results.append("Win")
  elif dealertotal < total and total <= 21:
    results.append("Win")
  else:
    results.append("Draw")

  Dealer = ["-", "-", cards[1], "-", cards[3]]
  hand.pop(0)
  hand.pop(0)
  Player = ["Hand", cards[0], "-", cards[2], "-"]
  dealer_hand.pop(0)
  dealer_hand.pop(0)
  Action = ["Action", "-", "-", "Stand", " "]
  for i in range(len(options)-3):
    if len(hand) != 0:
      Player.append(hand.pop(0))
      Dealer.append("-")
      Action.append(action.pop(0))
    elif len(dealer_hand) != 0 and len(hand) == 0:
      Player.append("-")
      Dealer.append(dealer_hand.pop(0))
      Action.append("-")
    else:
      Player.append("-")
      Dealer.append("-")
      Action.append("-")
  Player.append(str(total))
  Dealer.append(str(dealertotal))
  Action.append(" ")

  Player.append(results[0])
  Dealer.append("-")
  Action.append("-")
   
  addToStandWin([cards[1], cards[3]],[cards[0], cards[2]],results, convertCard(cards[0])+convertCard(cards[2]))
  return {'Dealer'+str(scenarioInt): Dealer, 'Player'+str(scenarioInt): Player, "Act"+ str(scenarioInt):Action}
  
#************************************************************************CONVERT CARD TO ACTUAL INTEGER VALUE****************************************************************************************************************************************************************

# Standard Card Conversion Methods
#convert Card to its value
def convertCard(card):
  val = 0
  if len(card) == 3:
    val = card[0]+ card[1]
  else:
    if card[0] == 'K' or card[0] == 'Q' or card[0] == 'J':
      val = 10
    elif card[0] == 'A':
      val = 11
    else:
      val = card[0]
  return int(val)
  
#************************************************************************WHERE THE MAGIC HAPPENS****************************************************************************************************************************************************************

# retrieve all hands from file of hands
all_hands = []
with open('fileofmillionhands.txt', 'r') as fd:
   line = fd.readline()
   while line:
      line = fd.readline()
      all_hands.append(line.split())
all_hands.pop(len(all_hands)-1)
dfs = []
# Scenarios for file of hands
while (len(all_hands) != 0):
  scenarioInt = " "
  #get hand
  options = all_hands.pop(0)

  # add this hand to Frequency Table

  addToFreq([options[0],options[2]], [options[1],options[3]], convertCard(options[0])+convertCard(options[2]))

  # Formatting for Cards in Scenario DataFrame
  dataOptions = ["-"]
  for i in options:
    dataOptions.append(i)
  for i in range(3):
    dataOptions.append("-")
  # Add Cards to data array for Dataframe
  data = {'Cards': dataOptions}
  total = convertCard(options[0])+ convertCard(options[2])
  if total > 21 and (options[0][0] =='A' or options[2][0] == 'A'):
   total-=10

  # Run each scenario option 
  # Run Hit (H)
  data.update(Hit(options))
  # Run Double Down
  
  if total == 9 or total == 10 or total == 11:
   data.update(DoubleDown(options))
  elif options[0][0] == 'A' or options[2][0] == 'A':
   data.update(DoubleDown(options))
  #Run Stand
  data.update(Stand(options))
  #Run Split 
  if options[0][0] == options[2][0]:
   data.update(Split(options))
  # Formatting for creating space between Scenarios
  free = ["     "] * 24
  data.update({scenarioInt:free})
  scenarioInt+=" "
  # add Dataframe for this hand to list of dataframes 
  df = pd.DataFrame.from_dict(data)
  dfs.append(df)

#Add Scenarios to Different CSV Files 
hands = 1
draftStrategyTable()
strategy_table.to_csv("../Blackjack Strategy Table.csv", index=False)
freq_df.to_csv("Frequency Table.csv", index=False)
win_dd_df.to_csv("Double Down Winning Hands Table.csv", index=False)
win_hit_df.to_csv("Hit Winning Hands Table.csv", index=False)
win_split_df.to_csv("Split Winning Hands Table.csv", index=False)
win_stand_df.to_csv("Stand Winning Hands Table.csv", index=False)
winning_strategy_table.to_csv("Winning Hands Table.csv", index=False)
probability_strategy_table.to_csv("Probability Table.csv", index=False)

  #for df in dfs:
    #Add each sheet as new Hand
    #df.to_excel(writer, sheet_name="Hand #"+str(hands), index=False)
    #print("end{}".format(hands))
    #hands+=1
