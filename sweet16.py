from numpy.random import choice

##### Odds to make it to elite 8

# 1 odds: 69.1%
# 5 odds: 5.9%
prob5v1 = [(69.1/75), (5.9/75)]

# 6 odds: 10.3%
# 2 odds: 45.6%
prob6v2 = [(45.6/55.9), (10.3/55.9)]

# 1 odds: 69.1%
# 4 odds: 15.4%




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

## 5 vs 1
seeds51E = ['Duke', 'Mississippi State']
draw51E = choice(seeds51E, 1, True, prob5v1)
print(draw51E)

# 6 vs 2
seeds62E = ['Michigan St', 'Maryland']
draw62E = choice(seeds62E, 1, True, prob6v2)
print(draw62E)


print(" ")
print(" ")



######################################
############# WEST SIDE ##############
######################################
# 1 vs 4

