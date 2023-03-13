import random
from numpy.random import choice
import pandas as pd

#Read Data
# threePoint = pd.read_csv('Data/3PPCT.csv')


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

    while i < 25:

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

def firstSouthRound():
    print('SOUTH: First Round')
    ## 16 vs 1
    # No. 1 seeds are 135-1 against No. 16 seeds
    compete('Alabama', 1, 'SMO', 16)

    # 8 vs 9
    compete('Maryland', 8, 'West Virginia', 9)

    # 12 vs 5
    compete('San Diego St.', 5, 'Charleston', 12)

    # 13 vs 4
    compete('Virginia', 4, 'Furman', 13)

    ## 11 vs 6
    compete('Creighton', 6, 'NC State', 11)

    # 14 vs 3
    compete('Baylor', 3, 'UCSB', 14)


    ## 10 vs 7
    compete('Missouri', 7, 'Utah St.', 10)

    ## 15 vs 2

    compete('Arizona', 2, 'Princeton', 15)


    print(" ")
    print(" ")

######################################
############# EAST SIDE #############
######################################

def firstEastRound():
    print('EAST: First Round')
    ## 16 vs 1
    # No. 1 seeds are 135-1 against No. 16 seeds
    compete('Purdue', 1, 'FDU', 16)

    # 8 vs 9
    compete('Memphis', 8, 'FAU', 9)

    # 12 vs 5
    compete('Duke', 5, 'Oral Roberts', 12)

    # 13 vs 4
    compete('Tennessee', 4, 'Louisiana', 13)

    ## 11 vs 6
    compete('Kentucky', 6, 'Providence', 11)

    # 14 vs 3
    compete('Kansas St.', 3, 'Montanta St.', 14)


    ## 10 vs 7
    compete('Michigan St.', 7, 'USC', 10)

    ## 15 vs 2

    compete('Marquette', 2, 'Vermont', 15)


    print(" ")
    print(" ")


######################################
############# WEST SIDE ##############
######################################


def firstWestRound():
    print('WEST: First Round')
    ## 16 vs 1
    # No. 1 seeds are 135-1 against No. 16 seeds
    compete('Kansas', 1, 'Howard', 16)

    # 8 vs 9
    compete('Arkansas', 8, 'Illinois', 9)

    # 12 vs 5
    compete("Saint Mary's", 5, 'VCU', 12)

    # 13 vs 4
    compete('UConn', 4, 'Iona', 13)

    ## 11 vs 6
    compete('TCU', 6, 'ASU', 11)

    # 14 vs 3
    compete('Gonzaga', 3, 'Grand Canyon', 14)


    ## 10 vs 7
    compete('Northwestern', 7, 'Boise St.', 10)

    ## 15 vs 2

    compete('UCLA', 2, 'UNC Asheville', 15)


    print(" ")
    print(" ")


######################################
########### MIDWEST SIDE #############
######################################


## 16 vs 1
# No. 1 seeds are 135-1 against No. 16 seeds
def firstMWRound():
    print('MIDWEST: First Round')
    ## 16 vs 1
    # No. 1 seeds are 135-1 against No. 16 seeds
    compete('Houston', 1, 'FDU', 16)

    # 8 vs 9
    compete('Iowa', 8, 'Auburn', 9)

    # 12 vs 5
    compete('Miami', 5, 'Drake', 12)

    # 13 vs 4
    compete('Indiana', 4, 'Kent St.', 13)

    ## 11 vs 6
    compete('Iowa St.', 6, 'Pittsburgh', 11)

    # 14 vs 3
    compete('Xavier', 3, 'Kennesaw St.', 14)


    ## 10 vs 7
    compete('Texas A&M', 7, 'Penn St.', 10)

    ## 15 vs 2

    compete('Texas', 2, 'Colgate', 15)


    print(" ")
    print(" ")


def firstRound():
    firstSouthRound()
    firstMWRound()
    firstWestRound()
    firstEastRound()


firstRound()
