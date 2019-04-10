from numpy.random import choice

##### Odds to make it to finals

# odds 1: 15.4%
# odds 2: 3.7%
probsFinal = [(15.4/19.1), (3.7/19.1)]

## Will use choices when this is 1
Ready = ['1' , '0']
probsReady = [.2, .8]
drawReady = choice(Ready, 1, True, probsReady)
print(drawReady)

print(" ")
print(" ")

seeds = ['Gonzaga', 'Kentucky']
draw = choice(seeds, 1, True, probsFinal)
print(draw)


