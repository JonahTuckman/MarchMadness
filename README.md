# MarchMadness
Using seeding probability and different data sources to build a March Madness Bracket

I have been in the bottom 10% of my families march madness pool for the past five years because of my limited college basketball knowledge.
I am hoping that this year, a bracket based on the seeding probabilities rather than the teams playing will prove to be accurate.

All probabilities used are according to the lower seeded teams odds of advancing. This is to account for the under-seeded teams not being unaccounted.

I used KenPom offensive and defensive rating, freethrow percentage, three point percentage, and win margin to provide scores to each team then coninutally run simulated games to visualize randomized outcomes.

Probability used for first two rounds: https://www.betfirm.com/seeds-national-championship-odds/

Running each program in terminal in order of:
    firstround.py -> roundof32.py -> sweet16.py -> elite8.py -> finalfour.py -> Finals.py
Running while filling out bracket then creating next script with odds adjusted to former predictions.
