import random
from numpy.random import choice
import pandas as pd

# Import Data
threePoint = pd.read_csv('../Data/3PPCT.csv')
freeThrow = pd.read_csv('../Data/FTPCT.csv')

KPAdjO = pd.read_csv('../Data/KPAdjO.csv')
KPAdjO = KPAdjO.drop(['Rk', 'Conf', 'W-L', 'AdjEM', 'AdjO', 'AdjT', 'Luck', 'AdjEM.1', 'OppO', 'OppD', 'AdjEM.2', 'AdjD'], axis = 1)

KPAdjD = pd.read_csv('../Data/KPAdjD.csv')
KPAdjD = KPAdjD.drop(['Rk', 'Conf', 'W-L', 'AdjEM', 'AdjO', 'AdjT', 'Luck', 'AdjEM.1', 'OppO', 'OppD', 'AdjEM.2', 'AdjD'], axis = 1)

scoringMargin = pd.read_csv('../Data/scoringMargin.csv')

# Assigning a score to each team based on their KenPom O and D rankings

def AssignKPScoreO(Team):
    score = 0
    for index, row in KPAdjO.iterrows():
        if Team.lower() == row['Team'].lower():
            score += (200 - index)
    return score / 200

def AssignKPScoreD(Team):
    score = 0
    for index, row in KPAdjD.iterrows():
        if Team.lower() == row['Team'].lower():
            score += (200 - index)
    return score / 200

# Assigning a score based on freethrow rankings

def AssignFTScore(Team):
    score = 0
    for index, row in freeThrow.iterrows():
        if Team.lower() == row['Team'].lower():
            score += (200 - index)
    return score / 200

# Assigning a score based on three point rankings

def Assign3PTScore(Team):
    score = 0
    for index, row in threePoint.iterrows():
        if Team.lower() == row['TEAM'].lower():
            score += (200 - index)
    return score / 200

# Assigning a score based on Margin of victory
def AssignMargin(Team):
    score = 0
    for index, row in scoringMargin.iterrows():
        if Team.lower() == row['TEAM'].lower():
            score += (200 - index)
    return score / 200

# Ranking Probabilities

# prob16 = [(127/128), (1/128)]
# prob8 = [57/128, 71/128]
# prob12 = [(84/128), (44/128)]
# prob13 = [100/128, 28/128]
# prob11 = [81/128, 47/128]
# prob14 = [(110/128), (18/128)]
# prob10 = [(75/128), (52/128)]
# prob15 = [(121/128), (7/128)]

# Score based on ranking history
def rankingScoreFirst(rank):
    if rank == 1:
        return (127/128)
    if rank == 16:
        return (1/128)
    if rank == 2:
        return (121/128)
    if rank == 15:
        return (7/128)
    if rank == 3:
        return (110/128)
    if rank == 14:
        return(18 / 128)
    if rank == 4:
        return (100/128)
    if rank == 13:
        return (28 / 128)
    if rank == 5:
        return (84/128)
    if rank == 12:
        return (44/128)
    if rank == 6:
        return (81/128)
    if rank == 11:
        return (47/128)
    if rank == 7:
        return (75/128)
    if rank == 10:
        return (52/128)
    if rank == 8:
        return(57/128)
    if rank == 9:
        return (71/128)

# First round score
def AssignScoreFirst(Team, Rank):
    score = (AssignKPScoreD(Team) + (AssignKPScoreO(Team) * 1.2) + Assign3PTScore(Team) + AssignFTScore(Team) + (rankingScoreFirst(Rank) * 1.5) + AssignMargin(Team))
    return score

# Run randomizer multiple times to eliminate some level of randomness (but not too much to keep some level)
def compete(Team1, seed1, Team2, seed2):
    score1 = AssignScoreFirst(Team1, seed1)
    score2 = AssignScoreFirst(Team2, seed2)
    total = score1 + score2
    i = 0
    team1Count = 0
    team2Count = 0
    winner = pd.DataFrame(columns = ['Team', 'Seed'])

    while i < 1000:

        num = random.uniform(0, total)


        if num < max(score1, score2):
            team1Count += 1
        else:
            team2Count += 1

        i += 1

    if team1Count > team2Count:
        print("Winner: " + Team1 + "," " Rank " + str(seed1))
    else:
        print("Winner: " + Team2 + "," " Rank " + str(seed2))

######################################
############# SOUTH SIDE #############
######################################

def sideOne():

    compete('Alabama', 1, 'Marquette', 2)


    print("")
    print("")


######################################
############# WEST SIDE #############
######################################

def sideTwo():

    compete('Kansas', 1, 'Texas', 2)


    print("")
    print("")



def finalFour():
    sideOne()
    sideTwo()



finalFour()
