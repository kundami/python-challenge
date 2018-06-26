CodeFight Solutions

Given an array of integers numbers, we'd like to find the closest pair of elements that add up to sum. Return the distance between the closest pair (absolute difference between the two indices). If there isn't a pair that adds up to sum, return -1.

numbers: [1, 0, 2, 4, 3, 0]
For numbers = [1, 0, 2, 4, 3, 0] and sum = 5 the output should be findClosestPair(numbers, sum) = 2


def findClosestPair(numbers, sum):
    closest_pair=999
    for i in range(0,len(numbers)):
        #print("numbers"+str(numbers[i]))
        stack = []
        add=numbers[i]
        for j in range(i+1,len(numbers)):
            #print("numbers inner"+str(numbers[j]))
            add = add+numbers[j]
            #print("add"+str(add))
            if add < sum :
                continue
            if add == sum :
             #   print("found match")
                if closest_pair > (j-i):
                    closest_pair = (j-i)
                else:
                    closest_pair = closest_pair
            if add > sum :
                add = add-numbers[j]
    if closest_pair == 999:
        return -1
    else:
        return closest_pair

Problem -2
For transactions = [1, 1, 2, -3, 0, 1000, 6, -6, 1, 1, 1, -3, 2], the output should be
zeroProfitPeriods(transactions) = 4.
The periods [1, 2, -3], [0], [6, -6], [1, 1, 1, -3] are each zero-profit. Also, the periods [1, 2, -3], [0], [6, -6], [1, -3, 2] are zero-profit as well. 

Did not work for:
transactions: [1, 1, -2, -2, -2, 1, 1, 1, -2, 1, -2, 1, 1, 1, -2, 1, 1, 1, 1, 1, 1, -2, -2, 1, 1, 1, -2, 1, 1, -2]
ans -8 

 def zeroProfitPeriods(transactions):
   zeroProfitPeriods=0
   sum = 99
   i = 0
   index=0
   while i < len(transactions):
      sum = transactions[i]
      bucket = []
      bucket.append(transactions[i])
      print("i is-"+str(i))
      if sum == 0 :
          zeroProfitPeriods = zeroProfitPeriods + 1
          i=i+1
          continue 
      j=i+1
      while j< len(transactions):
         if ( sum == 0 ):
            #Found a set of transactions with 0
            zeroProfitPeriods = zeroProfitPeriods + 1  
            print("J is-"+str(j))
            print("zeroProfitPeriods is"+str(zeroProfitPeriods))
            print(bucket)    
            i=i+len(bucket)-1
            break
         sum = sum + transactions[j]
         bucket.append(transactions[j])
         j=j+1 
      i=i+1
   return zeroProfitPeriods   


Mr. Hudson wants to take up as little class time as possible for the whole class to give their presentations. Return the total minimum number of minutes the presentations will be expected to take if the groups are assigned in such a way that the estimated total time is minimized.
Example
For timeEstimates = [12, 7, 3, 6, 5, 6, 10, 3, 9, 6] and groupSize = 3, the output should be assignGroups(timeEstimates, groupSize) = 28.
Here's one way the groups could be assigned for a minimal total time:


def assignGroups(timeEstimates, groupSize):
    # max number of group sizes
    # sort by max to min
    sorted_est = sorted(timeEstimates, reverse=True)
    # create buckets of group of max groupSize and then find min. 
    i=0  
    min_time=0
    while i < len(sorted_est) :
        buckets= []
        while len(buckets) < groupSize and i < len(sorted_est):
            #print("i-"+str(i))
            buckets.append(sorted_est[i])
            i=i+1   
        #Now for each bucket find the maxtime and add it min_time
        sorted_bucket = sorted(buckets, reverse=True)
        print(sorted_bucket)
        min_time=min_time+sorted_bucket[0]
        
    return min_time

http://ergast.com/api/f1/drivers.json?callback=myParser

https://ergast.com/api/f1/2008/5/results.json?callback=myParser

Example
For year = 2008, round = 5, and userBets = [[["massa", "2", "200"], ["webber", "7", "100"], ["alonso", "1", "100"]], [["massa", "1", "200"]]], the output should be formulaOneBet(year, round, userBets) = 200.
The first user gets 2 winning bets (for massa and webber). All the money 200 + 100 + 100 + 200 = 600 are divided in proportion 2:1 for these winning bets. The first user earns 600 - 400 = 200, and the second users earns 0 - 200 = -200, so 200 is the largest earned amount.
For year = 2008, round = 5, and userBets = [[["massa", "2", "200"]], [["webber", "7", "100"]]], the output should be formulaOneBet(year, round, userBets) = 0.
Both users get winning bets. All the money 200 + 100 = 300 are divided in propotion 2:1 for this winning bets. The first user earns 200 - 200 = 0, and the second user earns 100 - 100 = 0, so the largest earned amount is 0.
For year = 2017, round = 1, and userBets = [[["michael_schumacher", "6", "500"]]], the output should be formulaOneBet(year, round, userBets) = -500.

import requests
def formulaOneBet(year, round, userBets):
    #make the api call..
    series="f1"
    getstr="https://ergast.com/api/"+series+"/"+str(year)+"/"+str(round)+"/results.json?callback=myParser"
    r =requests.get(getstr)
    #response = json.load(r)
    print(getstr)
    #Find winning bets
    #Find who made the winning bets
    #Calculate earning and spent.
    return 200


import requests
def formulaOneBet(year, round, userBets):
    #create a dict for each user..
    user_dict = {}
         
    #make the api call..
    series="f1"
    driver_dict ={}
    getstr="https://ergast.com/api/"+series+"/"+str(year)+"/"+str(round)+"/results.json"
    r =requests.get(getstr)
    json_str= r.json()
    data = json_str['MRData']['RaceTable']['Races']
    for i in range(len(data)):
        #print("key:"+str(data[i]))
        data_dict =  data[i]
        for key,value in data_dict.items():
            #print("key:"+str(key))
            if key == 'Results':
                results = value
                for i in range(len(results)):
                    parse = results[i]
                    driver = parse['Driver']
                    #print(driver['driverId'])
                    driver_dict[driver['driverId']] =  parse['position']
                    
    print(driver_dict)                
    user_cost = {}
    user_won={} 
    win_bets={}
    all_money = 0
    win_amount = 0
    max_profit= 0
    for i in range(len(userBets)):
        user_bet = userBets[i]    
        win_count = 0
        bet_amount = 0
        user_won[i+1] = 0
        win_amount_each=0
        for j in range(len(user_bet)):
            bets = user_bet[j]
            bet_driver = bets[0]
            bet_position = bets[1]
            bet_amount = bet_amount+ int(bets[2])
            user_cost[i+1] = bet_amount
            max_profit=-bet_amount
            all_money = all_money + bet_amount
            #print("bet driver:"+bet_driver) 
            if(bet_driver in driver_dict and driver_dict[bet_driver] == bet_position ):
                print("user:"+str(i+1)+"win:"+bet_driver+"pos"+str(bet_position))
                win_count = win_count+1
                user_won[i+1]= win_count
                win_amount = win_amount+int(bets[2])
                win_amount_each = win_amount_each + int(bets[2])
                win_bets[i+1] = win_amount_each
                
                
                
    #now calculate net profit per user and max..
    print("win amt:"+str(win_amount))
    print("all money:"+str(all_money))
    no_wins = len(user_won)
    print(win_bets)
    print(user_won)
    print(user_cost)
    #win_share=user_cost[key]
    for key, value in user_won.items():
        print('key:'+str(key),"Value:"+str(value))
        if key in win_bets:
            win_bet_wage = win_bets[key]
            user_cost_each = user_cost[key]
            win_share = all_money*(win_bet_wage/win_amount)-user_cost_each
            print(str(win_share))
            if max_profit < win_share :
                print("max profit:", max_profit)
                max_profit = win_share
    

        #    print(data)
    #Find winning bets
    #Find who made the winning bets
    #Calculate earning and spent.
    return max_profit


For terrainDifficulty = [3, 5, 4, 2, 3, 1, 5, 3, 4] and energy = 11, the output should be roverTour(terrainDifficulty, energy) = 4.

def roverTour(terrainDifficulty, energy):
    maxrun=0
    for i in range(0,len(terrainDifficulty)):
        #maxrun=0
        energy_spent=terrainDifficulty[i]
        #print("en:",str(energy_spent))
        run=0   
        for j in range(i+1,len(terrainDifficulty)):
            energy_spent=energy_spent+terrainDifficulty[j]
           # print("ene sp:",str(energy_spent))
            if energy_spent <= energy:
                #print('i:'+str(i), "j:"+str(j)+"ene:"+str(energy_spent))
                #check if we have exceeded maxrun and reset it
                run=j-i+1
                if run > maxrun:
                 #   print('run:', str(run))
                    maxrun=run
                    continue
            else:
                break       
    if (maxrun==0):
        for i in range(0,len(terrainDifficulty)):
            if terrainDifficulty[i] < energy:
                maxrun=1
    return maxrun        
    

    import string

#For number = "121", base1 = 4, and base2 = 2, the output should be mirrorBase(number, base1, base2) = false.

#121 in base 4 is 1 * 16 + 2 * 4 + 1 * 1 = 25, and in base 2, that's 11001, which is not a palindrome.#

#For number = "505", base1 = 6, and base2 = 7, the output should be mirrorBase(number, base1, base2) = true.

#505 in base 6 is 5 * 36 + 0 * 6 + 5 * 1 = 185, and in base 7, that's 353, which is a palindrome.

import string
# Possible digits from the lowest to the highest

def mirrorBase(number, base1, base2):
    known_digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    value  = { ch:val for val,ch in enumerate(known_digits) if val<base1 }
    num_str = str(number)
    leng = len(str(num_str))
    num = 0
    power=1
    for i in range(len(number),0,-1):
        try:
            d = number[i-1]
            num = num + (int(value[d]) * power)
            print("value-"+number[i-1]+"num:"+str(num))
        except ValueError:
            print("value Error-"+number[i-1])
            continue
        power=power*base1
    assert(num >= 0)
    assert(1< base2 < 37)
    r = ''
    while num > 0:
        r = string.printable[num % base2] + r
        num //= base2
    print("res-"+str(r))
    if r == str(r)[::-1]:
        return True
    else :
        return False
    
You're a pretty fast typer - each keystroke takes you 75 milliseconds, but if you're able to use a different hand than the previous key, it only takes you 50.

You use your left hand for the Q, W, E, R, T, A, S, D, F, G, Z, X, C, V, and B keys, and you use your right hand for the Y, U, I, O, P, H, J, K, L, N, and M keys. You can use either hand for the spacebar.

keyboard layout
Note: for the purpose of this challenge, we'll ignore all other keys.

Given a string text, find the shortest time it'll take for you to type it out (in milliseconds). The first keystroke always takes 50ms.

Example

For text = "abc", the output should be alternatingKeys(text) = 200.

The first keystroke always takes 50ms, but since you need to use your left hand again for the b and c keys, each of those keystrokes will take 75ms, for a total of 50 + 75 + 75 = 200.

For text = "land", the output should be alternatingKeys(text) = 200.

Again, the first keystroke will take 50ms, but since each key alternates between your left and right hand, they'll each only take 50ms, for a total of 50 + 50 + 50 + 50 = 200.

import string
def alternatingKeys(text):
    left = ['Q', 'W', 'E', 'R', 'T', 'A', 'S', 'D', 'F', 'G', 'Z','X','C','V','B' ]
    right = ['Y', 'U', 'I', 'O', 'P', 'H', 'J', 'K', 'L', 'N',  'M' ]
    up_text = text.upper()
    print(up_text)
    order =[]
    last_key=''
    for i in range(0,len(text)):
        print(up_text[i])
        if up_text[i] in left:
            order.append('L')
            last_key='L'
        if up_text[i] in right:
            order.append('R')
            last_key='R'
        if up_text[i].isspace():
            #print("I am here"+last_key)
            if last_key == 'L':
                order.append('R')
                last_key = 'R'
                continue
            if last_key == 'R':
                order.append('L')
                last_key = 'L'
                continue
            else :
                order.append('L')
                last_key = 'L'
                
    time=0
    last_key=''
    for i in range(0,len(order)):
        if i == 0:
            time=50
        else:    
            if order[i] == last_key:
                time = time + 75
            else:
                time = time + 50
        last_key = order[i]
       

    return time


from collections import Counter

def recur(res, dices):
    size = len(dices)
    res1 = []
    #print("$here:"+str(res))
           
    if size == 0:
        return res
    if res:
        #print("Ins")
        for i in range(0,len(res)):
            dice=dices[0]
            #print(dice)
            for j in range(0,len(dice)):
                valu =res[i]+dice[j]
                res1.append(valu)
        res = res1
        return recur(res,dices[1:size])
    else:
        #print("There")
        res = dices[0][:]
        return recur(res,dices[1:size])
    return res
            

def diceRolls2(dice):
    res=[]
    value=recur(res,dice)
    count = Counter(value)
    x,y = count.most_common()[0]
    return x