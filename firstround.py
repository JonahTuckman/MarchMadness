import random
from numpy.random import choice


## Global Probabilities
prob16 = [(135/136), (1/136)]
prob8 = [.50, .50]
prob12 = [(89/136), (47/136)]
prob13 = [.79, .21]
prob11 = [.625, .375]
prob14 = [(115/136), (21/136)]
prob10 = [(84/136), (52/136)]
prob15 = [(128/136), (8/136)]


## Will use choices when this is 1
Ready = ['1' , '0']
probsReady = [.2, .8]
drawReady = choice(Ready, 1, True, probsReady)
print(drawReady)

print(" ")
print(" ")

######################################
############# EAST SIDE ##############
######################################


## 16 vs 1
# No. 1 seeds are 135-1 against No. 16 seeds
seeds16E = ['Duke', 'NDS']
draw16E = choice(seeds16E, 1, True, prob16 )
print(draw16E)


# 8 vs 9
# 50/50 proposition, as No. 8 and No. 9 seeds have split their 136 meetings since 1985
seeds8E = ['VCU', 'UCF']
draw8E = choice(seeds8E, 1, True, prob8)
print(draw8E)

# 12 vs 5
# 47 upsets since 1985. That is 136 games
seeds12E = ['Mississippi State', 'Liberty']
draw12E = choice(seeds12E, 1, True, prob12)
print(draw12E)

# 13 vs 4
## upset 21 percent of the time
seeds13E = ['Virginia Tech', 'Saint Louis']
draw13E = choice(seeds13E, 1, True, prob13)
print(draw13E)

## 11 vs 6
## 51 out of 136 opening round match-ups, or 37.5 percent of the time.
seeds11E = ['Maryland', 'Belmont']
draw11E = choice(seeds11E, 1, True, prob11)
print(draw11E)

# 14 vs 3
## 21/136 all time
seeds14E = ['LSU', 'Yale']
draw14E = choice(seeds14E, 1, True, prob14)
print(draw14E)

## 10 vs 7
## 10 seeds are 52-84 against 7 seeds
seeds10E = ['Louisville', 'Minnesota']
draw10E = choice(seeds10E, 1, True, prob10)
print(draw10E)

## 15 vs 2
## 8-128 all time
seeds15E = ['Michigan State', 'Bradley']
draw15E = choice(seeds15E, 1, True, prob15)
print(draw15E)



print(" ")
print(" ")

######################################
############# SOUTH SIDE #############
######################################


## 16 vs 1
# No. 1 seeds are 135-1 against No. 16 seeds
seeds16S = ['Virginia', 'Gardner-Webb']
draw16S = choice(seeds16S, 1, True, prob16 )
print(draw16S)


# 8 vs 9
# 50/50 proposition, as No. 8 and No. 9 seeds have split their 136 meetings since 1985
seeds8S = ['Ole Miss', 'Oklahoma']
draw8S = choice(seeds8S, 1, True, prob8)
print(draw8S)

# 12 vs 5
# 47 upsets since 1985. That is 136 games
seeds12S = ['Wisconsin', 'Oregon']
draw12S = choice(seeds12S, 1, True, prob12)
print(draw12S)

# 13 vs 4
## upset 21 percent of the time
seeds13S = ['Kansas State', 'Uc Irvine']
draw13S = choice(seeds13S, 1, True, prob13)
print(draw13S)

## 11 vs 6
## 51 out of 136 opening round match-ups, or 37.5 percent of the time.
seeds11S = ['Villanova', 'Saint Marys']
draw11S = choice(seeds11S, 1, True, prob11)
print(draw11S)

# 14 vs 3
## 21/136 all time
seeds14S = ['Purdue', 'Old Dominion']
draw14S = choice(seeds14S, 1, True, prob14)
print(draw14S)

## 10 vs 7
## 10 seeds are 52-84 against 7 seeds
seeds10S = ['Cincinnati', 'Iowa']
draw10S = choice(seeds10S, 1, True, prob10)
print(draw10S)

## 15 vs 2
## 8-128 all time
seeds15S = ['Tennessee', 'Colgate']
draw15S = choice(seeds15S, 1, True, prob15)
print(draw15S)


print(" ")
print(" ")
