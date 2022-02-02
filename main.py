import copy
import random
import os
# playerRuns = random.randint(0,120)
# playerBowls = round((100/random.randint(90,250))*playerRuns)
a = {43:28,13:14,59:33,21:16,4:5,7:4,38:29,42:22,9:8,2:5,4:6}
aCtual = {}
bowls = 0
for playerRuns,playerBowls in a.items():
    boundariesPercentage = [random.randint(30,60),random.randint(20,40),random.randint(14,25),random.randint(1,3),random.randint(8,20),random.randint(2,8)]
    def clearit():
        strikerate = round(((playerRuns/playerBowls)*100))
        if strikerate > 150:
            boundariesPercentage[5]+=random.randint(4,10)
            boundariesPercentage[0]-=random.randint(4,9)
            boundariesPercentage[4]+=random.randint(4,15)
            boundariesPercentage[2]+=random.randint(1,3)
            boundariesPercentage[1]+=random.randint(1,11)
        if strikerate > 100 and strikerate<150:
            boundariesPercentage[5]+=random.randint(2,4)
            boundariesPercentage[0]-=random.randint(1,4)
            boundariesPercentage[4]+=random.randint(3,8)
            boundariesPercentage[2]+=random.randint(1,3)
            boundariesPercentage[1]+=random.randint(1,9)
        if strikerate > 80 and strikerate<100:
            boundariesPercentage[5] = 3
            boundariesPercentage[0]+=random.randint(5,9)
            boundariesPercentage[2]-=random.randint(1,2)
            boundariesPercentage[1]+=random.randint(1,6)
        if strikerate > 60 and strikerate<80:
            boundariesPercentage[5] = 2
            boundariesPercentage[0]+=random.randint(7,12)
            boundariesPercentage[4]-=random.randint(1,3)
            boundariesPercentage[2]-=random.randint(1,3)
            boundariesPercentage[1]+=random.randint(1,5) 
        if strikerate<50:
            boundariesPercentage[4]+=random.randint(2,5)
            boundariesPercentage[5]=1 

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
    # print(sum(playerApproach))
    bowler = []
    def giveVar():
        return copy.deepcopy(playerApproach)
    def checkPercentage(n,m):
        mCount = 0
        for i in n:
            if i == m:
                mCount+=1
        return round((mCount/len(n))*100)
    overs = {}
        
    overRuns = 0

    tempIs = False
    while bowls<=120:
        try:
            playerApproach1 = giveVar()
            # print(playerApproach1)
            random.shuffle(playerApproach1)
            if player[1]%6 == 0 and player[1]!=0 and tempIs==False:
                bowlerName = input("Enter the name of the bowler that bowled previous over: ")
                try:
                    overs[bowlerName] = [overs[bowlerName][0]+overRuns,overs[bowlerName][1]+1]
                    overRuns = 0
                except:
                    overs[bowlerName] = [overRuns,1]
                    overRuns = 0
        
            userChoice = int(input("enter your bowling choice: "))
            os.system("clear")
            
            if len(bowler)>4 and checkPercentage(bowler,userChoice) > 30:
                print(f"Can't bowl {userChoice} rn\nTry another number")
                tempIs = True
            else:
                bowler.append(userChoice)
                
                if userChoice>6 or userChoice<1 or userChoice==5:
                    continue
                else:
                    playerChoice = ""
                    try:
                        playerChoice = random.choice(playerApproach1)
                    except:
                        playerApproach1 = giveVar()
                        playerChoice = random.choice(playerApproach1)

                    playerApproach1.remove(playerChoice)
                    if userChoice == playerChoice:
                        playerLifes-=1
                        if playerLifes==0:
                            print(f"Player out!\nPlayer runs and bowls{player}\nPlayer boundaries: {choices}")  
                            tempIs = False
                            aCtual[player[0]] = player[1]
                            bowls+=1
                            bowlerName = input("Enter the name of the bowler that bowled previous over: ")
                            toUpdate = float(f"0.{player[1]%6}")
                            if player[1]%6 == 0:
                                toUpdate = 1
                            try:
                                overs[bowlerName] = [overs[bowlerName][0]+overRuns,overs[bowlerName][1]+toUpdate]
                            except:
                                overs[bowlerName] = [overRuns,toUpdate]
                            break
                        else:
                            print("ONE LIFE GONE")
                            print(f"life remaining: {playerLifes}")
                            player[1]+=1
                            choices[0]+=1
                            bowls+=1
                            tempIs = False
                            print(f"Runs and Bowls: {player}\nPlayer Wheel: {choices}")
                    else:
                        player[0]+=playerChoice
                        player[1]+=1
                        bowls+=1
                        choices[playerChoice]+=1
                        overRuns+=playerChoice
                        tempIs = False
                        print(f"Runs and Bowls: {player}\nPlayer Wheel: {choices}")
        except:
            break

print(aCtual)
# hey
print(overs)