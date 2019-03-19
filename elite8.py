from numpy.random import choice

##### Odds to make it to final 4

# 1 odds: 41.2%
# 6 odds: 2.2%
prob1v6 = [(41.2/43.4), (2.2/43.4)]

# 1 odds: 41.2%
# 3 odds: 11.8%
prob1v3 = [(41.2/53), (11.8/53)]

# 1 odds: 41.2%
# 2 odds: 20.6%
prob1v2 = [(41.2/61.8), (20.6/61.8)]

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

# 1 vs 6
seeds61E = ['Duke', 'Maryland']
draw61E = choice(seeds61E, 1, True, prob1v6)
print(draw61E)

print(" ")
print(" ")

######################################
############# WEST SIDE ##############
######################################

# 1 vs 3
seeds31W = ['Gonzaga', 'Texas Tech']
draw31W = choice(seeds31W, 1, True, prob1v3)
print(draw31W)

print(" ")
print(" ")

######################################
############ SOUTH SIDE ##############
######################################

# 1 vs 3
seeds31S = ['Virginia', 'Purdue']
draw31S = choice(seeds31S, 1, True, prob1v3)
print(draw31S)

print(" ")
print(" ")

######################################
########## MIDWEST SIDE ##############
######################################

# 1 vs 2
seeds21M = ['North Carolina', 'Kentucky']
draw21M = choice(seeds21M, 1, True, prob1v2)
print(draw21M)
