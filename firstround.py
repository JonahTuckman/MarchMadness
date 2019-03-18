import random
from numpy.random import choice

## 16 vs 1
# No. 1 seeds are 135-1 against No. 16 seeds
seeds16 = ['1', '16']
prob16 = [(135/136), (1/136)]
draw16 = choice(seeds16, 1, True, prob16 )
print(draw16)


# 8 vs 9
# 50/50 proposition, as No. 8 and No. 9 seeds have split their 136 meetings since 1985
seeds8 = ['8', '9']
prob8 = [.50, .50]
draw8 = choice(seeds8, 1, True, prob8)
print(draw8)

# 12 vs 5
# 47 upsets since 1985. That is 136 games
seeds12 = ['5', '12']
prob12 = [(89/136), (47/136)]
draw12 = choice(seeds12, 1, True, prob12)
print(draw12)

