from math import log
numOfPerson = int(input("Enter Number of Contestant :"))
distList = [float(x) for x in input("Enter space separated dist :").split(" ")]
strengthList = [int(x) for x in input("Enter space separated strength :").split(" ")]

minDist = min(distList)
maxDist = max(distList)

def getStrength(playerIndex, trophyDist):
    ret = log(2+abs(trophyDist-distList[playerIndex]),2)
    ret = strengthList[playerIndex]/ret
    return ret

def frange(a, b, stp=1.0):
  i = a+stp/2.0
  while i<b:
    yield a
    a += stp
    i += stp

def isSuitableTrophyDist(dist):
    forceList = []
    teamA = []
    teamB = []
    for player in range(0, numOfPerson):
        forceList.append(getStrength(player, dist))
        if (distList[player] < dist):
            teamA.append(player)
        else:
            teamB.append(player)
    teamAStrength = 0
    teamBStrength = 0
    for index in teamA:
        teamAStrength += forceList[index]
    for index in teamB:
        teamBStrength += forceList[index]
    #print(dist,teamAStrength,teamBStrength,len(teamA), len(teamB))
    return teamAStrength == teamBStrength



print(numOfPerson)
print(distList)
print(strengthList)

pos = 0
posList = []

for dist in frange(minDist, maxDist, 0.000000001):
    isSuitable = isSuitableTrophyDist(dist)
    if isSuitable:
        pos += 1
        posList.append(dist)
        print("Found value {}".format(dist))

print("Number of position : {}".format(pos))
print(posList)