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
prob4v1 = [(69.1/84.5), (15.4/84.5)]

# 2 odds: 45.6%
# 3 odds: 25.0%
prob3v2 = [(45.6/70.6), (25/70.6)]

# 3 odds: 25.0%
# 10 odds: 5.9%
prob10v3 = [(25/30.9), (5.9/30.9)]



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
seeds41W = ['Gonzaga', 'Florida St']
draw41W = choice(seeds41W, 1, True, prob4v1)
print(draw41W)

# 2 vs 3
seeds32W = ['Michigan', 'Texas Tech']
draw32W = choice(seeds32W, 1, True, prob3v2)
print(draw32W)


print(" ")
print(" ")



######################################
############# SOUTH SIDE #############
######################################

# 5 vs 1
seeds51S = ['Virginia', 'Wisconsin']
draw51S = choice(seeds51S, 1, True, prob5v1)
print(draw51S)

# 10 v 3
seeds103S = ['Purdue', 'Iowa']
draw103S = choice(seeds103S, 1, True, prob10v3)
print(draw103S)


print(" ")
print(" ")

######################################
########### MIDWEST SIDE #############
######################################

# 1 vs 4
seeds41M = ['North Carolina', 'Kansas']
draw41M = choice(seeds41M, 1, True, prob4v1)
print(draw41M)

# 2 vs 3
seeds32M = ['Kentucky', 'Houston']
draw32M = choice(seeds32M, 1, True, prob3v2)
print(draw32M)
