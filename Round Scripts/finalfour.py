from numpy.random import choice

##### Odds to make it to finals

# 1 vs 1 odds
prob1v1 = [.5,.5]

# 1 odds: 24.3%
# 2 odds: 9.6%
prob1v2 = [(24.3/33.9), (9.6/33.9)]

## Will use choices when this is 1
Ready = ['1' , '0']
probsReady = [.2, .8]
drawReady = choice(Ready, 1, True, probsReady)
print(drawReady)

print(" ")
print(" ")


######################################
############# LEFT SIDE ##############
######################################

seeds11L = ['Duke', 'Gonzaga']
draw11L = choice(seeds11L, 1, True, prob1v1)
print(draw11L)

print(" ")
print(" ")

######################################
############# WEST SIDE ##############
######################################

seeds12R = ['Virginia', 'Kentucky']
draw12R = choice(seeds12R, 1, True, prob1v2)
print(draw12R)
