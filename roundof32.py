from numpy.random import choice

## 9 have a probability of 5.1% of reaching sweet sixteen
prob9 = [.949, .051]

# 6 of 28 winning 13 seeds have then won another game
prob13 = [(22/28), (6/28)]

# Six seeds 30.9% chance of making sweet 16
prob6 = [.691, .309]

# Ten seeds have 16.9% chance to make it to sweet 16
prob10 = [.831, .169]

# 12 seeds have a probability of 14.7% of reaching sweet sixteen
prob12 = [.853, .147]

# 7 seeds have a 19.9% chance of reaching the sweet 16
prob7 = [.801, .199]


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

## 9 vs 1
seeds91E = ['Duke', 'UCF']
draw91E = choice(seeds91E, 1, True, prob9)
print(draw91E)

# 5 vs 13
seeds513E = ['Mississippi State', 'Saint Louis']
draw513E = choice(seeds513E, 1, True, prob13)
print(draw513E)


# 6 vs 3
seeds63E = ['LSU', 'Maryland']
draw63E = choice(seeds63E, 1, True, prob6)
print(draw63E)


seeds102E = ['Michigan State', 'Minnesota']
draw102E = choice(seeds102E, 1, True, prob10)
print(draw102E)


print(" ")
print(" ")

######################################
############# WEST SIDE ##############
######################################

## 9 vs 1
seeds91W = ['Gonzaga', 'Baylor']
draw91W = choice(seeds91W, 1, True, prob9)
print(draw91W)

# 12 vs 4
seeds124W = ['Florida State', 'Murray State']
draw124W = choice(seeds124W, 1, True, prob12)
print(draw124W)

# 6 vs 3
seeds63W = ['Texas Tech', 'Buffalo']
draw63W = choice(seeds63W, 1, True, prob6)
print(draw63W)

# 7 vs 2
seeds72W = ['Michigan State', 'Minnesota']
draw72W = choice(seeds72W, 1, True, prob7)
print(draw72W)
