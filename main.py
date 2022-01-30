from copy import copy
import random

playerRuns = random.randint(0,150)
playerBowls = round((100/random.randint(80,120))*playerRuns)
print(playerRuns)
print(playerBowls)
boundariesPercentage = [random.randint(30,60),random.randint(20,40),random.randint(14,25),random.randint(1,3),random.randint(8,20),random.randint(2,8)]
def clearit():
    strikerate = round(((playerRuns/playerBowls)*100))
    if strikerate > 150:
        boundariesPercentage[5]+=random.randint(4,10)
        boundariesPercentage[0]-=random.randint(4,9)
        boundariesPercentage[4]+=random.randint(4,10)
        boundariesPercentage[2]+=random.randint(1,5)
        boundariesPercentage[1]+=random.randint(1,8)
    if strikerate > 100 and strikerate<150:
        boundariesPercentage[5]+=random.randint(2,4)
        boundariesPercentage[0]-=random.randint(1,4)
        boundariesPercentage[4]+=random.randint(2,5)
        boundariesPercentage[2]+=random.randint(1,5)
        boundariesPercentage[1]+=random.randint(1,6)
    if strikerate > 80 and strikerate<100:
        boundariesPercentage[5] = 3
        boundariesPercentage[0]+=random.randint(5,9)
        boundariesPercentage[4]-=random.randint(1,3)
        boundariesPercentage[2]-=random.randint(1,4)
        boundariesPercentage[1]+=random.randint(1,4)
    if strikerate > 60 and strikerate<80:
        boundariesPercentage[5] = 2
        boundariesPercentage[0]+=random.randint(7,12)
        boundariesPercentage[4]-=random.randint(2,4)
        boundariesPercentage[2]-=random.randint(1,2)
        boundariesPercentage[1]+=random.randint(1,3)   
    

clearit()


def perc(n):
    return round((n/100)*playerBowls)
eachbowlPercentage = {0:perc(boundariesPercentage[0]),1:perc(boundariesPercentage[1]),2:perc(boundariesPercentage[2]),3:perc(boundariesPercentage[3]),4:perc(boundariesPercentage[4]),6:perc(boundariesPercentage[5])}
playerApproach = []

for i,j in eachbowlPercentage.items():
    for _ in range(j):
        playerApproach.append(i)
req = playerRuns-sum(playerApproach) 
if req!=0:
    if req<0:
        reqlist = []
        allZeroes = []
        for i in playerApproach:
            if i!=0:
                reqlist.append(i)
            elif i == 0:
                allZeroes.append(0)
        random.shuffle(reqlist)
        for i in reqlist:
            reqlist.remove(i)
            if sum(reqlist)<playerRuns:
                break
        requiredList = []
        for i in reqlist:
            requiredList.append(i)
        for i in allZeroes:
            requiredList.append(i)
        playerApproach = requiredList     
        # print(sum(playerApproach)) 
    elif req>0:
        pass

playerLifes = round(playerBowls/6)
player = [0,0]
choices = [0,0,0,0,0,None,0]
print(sum(playerApproach))
tempPlayer = copy.deepcopy(playerApproach)
while True:
    print(playerApproach)
    random.shuffle(playerApproach)
    userChoice = int(input("enter your bowling choice: "))
    if userChoice>6 or userChoice<1 or userChoice==5:
        continue
    else:
        playerChoice = ""
        try:
            playerChoice = random.choice(playerApproach)
        except:
            playerApproach = tempPlayer
            playerChoice = random.choice(playerApproach)

        playerApproach.remove(playerChoice)
        if userChoice == playerChoice:
            playerLifes-=1
            if playerLifes==0:
                print(f"Player out!\nPlayer runs and bowls{player}\nPlayer boundaries: {choices}")  
                break
            else:
                print("ONE LIFE GONE")
                print(f"life remaining: {playerLifes}")
                player[1]+=1
                choices[0]+=1
                print(f"Runs and Bowls: {player}\nPlayer Wheel: {choices}")
        else:
            player[0]+=playerChoice
            player[1]+=1
            choices[playerChoice]+=1
            print(f"Runs and Bowls: {player}\nPlayer Wheel: {choices}")




