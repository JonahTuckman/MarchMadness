from numpy.random import choice

##### Odds to make it to sweet 16

# 9 odds: 5.1%
# 1 odds: 85.3%
prob9v1 = [(85.3/90.4), (5.1/90.4)]

# 13 odds: 4.4%
# 5 odds: 33.8%
prob13v5 = [(33.8/38.2), (4.4/38.2)]

# 6 odds: 30.9%
# 3 odds: 51.5%
prob6v3 = [(51.5/82.4), (30.9/82.4)]

# 10 odds: 16.9%
# 2 odds: 62.5%
prob10v2 = [(62.5/79.4), (16.9/79.4)]

# 12 odds: 14.7%
# 4 odds: 47.1%
prob12v4 = [(47.1/61.8), (14.7/61.8)]

# 7 odds: 19.9
# 2 odds: 62.5
prob7v2 = [(62.5/82.4), (19.9/82.4)]


# 5 odds: 33.8%
# 4 odds: 47.1%
prob5v4 = [(47.1/80.9), (33.8/80.9)]

# 1 odds: 85.3%
# 8 odds: 9.6%
prob8v1 = [(85.3/94.9), (9.6/94.9)]

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
draw91E = choice(seeds91E, 1, True, prob9v1)
print(draw91E)

# 5 vs 13
seeds513E = ['Mississippi State', 'Saint Louis']
draw513E = choice(seeds513E, 1, True, prob13v5)
print(draw513E)


# 6 vs 3
seeds63E = ['LSU', 'Maryland']
draw63E = choice(seeds63E, 1, True, prob6v3)
print(draw63E)

# 10 vs 2
seeds102E = ['Michigan State', 'Minnesota']
draw102E = choice(seeds102E, 1, True, prob10v2)
print(draw102E)


print(" ")
print(" ")

######################################
############# WEST SIDE ##############
######################################

## 9 vs 1
seeds91W = ['Gonzaga', 'Baylor']
draw91W = choice(seeds91W, 1, True, prob9v1)
print(draw91W)

# 12 vs 4
seeds124W = ['Florida State', 'Murray State']
draw124W = choice(seeds124W, 1, True, prob12v4)
print(draw124W)

# 6 vs 3
seeds63W = ['Texas Tech', 'Buffalo']
draw63W = choice(seeds63W, 1, True, prob6v3)
print(draw63W)

# 7 vs 2
seeds72W = ['Michigan', 'Nevada']
draw72W = choice(seeds72W, 1, True, prob7v2)
print(draw72W)


print(" ")
print(" ")


######################################
############# SOUTH SIDE #############
######################################

## 9 vs 1
seeds91S = ['Virginia', 'Oklahoma']
draw91S = choice(seeds91S, 1, True, prob9v1)
print(draw91S)

# 5 vs 4
seeds54S = ['Kansas State', 'Wisconsin']
draw54S = choice(seeds54S, 1, True, prob5v4)
print(draw54S)

# 6 vs 3
seeds63S = ['Purdue', 'Villanova']
draw63S = choice(seeds63S, 1, True, prob6v3)
print(draw63S)

# 10 vs 2
seeds102S = ['Tennessee', 'Iowa']
draw102S = choice(seeds102S, 1, True, prob10v2)
print(draw102S)


print(" ")
print(" ")

######################################
############ MIDWEST SIDE ############
######################################

# 8 vs 1
seeds81M = ['North Carolina', 'Utah State']
draw81M = choice(seeds81M, 1, True, prob8v1)
print(draw81M)

# 5 vs 4
seeds54M = ['Auburn', 'Kansas']
draw54M = choice(seeds54M, 1, True, prob5v4)
print(draw54M)

# 6 vs 3
seeds63M = ['Houston', 'Iowa State']
draw63M = choice(seeds63M, 1, True, prob6v3)
print(draw63M)

# 10 vs 2
seeds102M = ['Kentucky', 'Seton Hall']
draw102M = choice(seeds102M, 1, True, prob10v2)
print(draw102M)
