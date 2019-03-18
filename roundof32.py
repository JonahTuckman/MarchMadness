from numpy.random import choice

## 9 seeds have lost lost 62 of 69 games
prob1v9 = [(62/69), (7/69)]
# 6 of 28 winning 13 seeds have then won another game
prob5v13 = [(22/28), (6/28)]

# Six seeds 30.9% chance of making sweet 16
prob6v3 = [.691, .309]

# Ten seeds have 16.9% chance to make it to sweet 16
prob10v2 = [.831, .169]

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
draw91E = choice(seeds91E, 1, True, prob1v9)
print(draw91E)

# 5 vs 13
seeds513E = ['Mississippi State', 'Saint Louis']
draw513E = choice(seeds513E, 1, True, prob5v13)
print(draw513E)


# 6 vs 3
seeds63E = ['LSU', 'Maryland']
draw63E = choice(seeds63E, 1, True, prob6v3)
print(draw63E)


seeds102E = ['Michigan State', 'Minnesota']
draw102E = choice(seeds102E, 1, True, prob10v2)
print(draw102E)
