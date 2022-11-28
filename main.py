import math as m

for i in range(200):
    n = i * 0.5
    if (m.floor(n) % 2) == 0:
        print(1 * m.fabs(n - (m.floor(n) + 1)) - ((1 - 1)/2))

    elif (m.floor(n) % 2) != 0:
        print(-1 * m.fabs(n - (m.floor(n) + 1)) - ((-1 - 1) / 2))
        #   i^(2*[[x]]) * | x - ([[x]] + 1)| - ((i^(2*[[x]]))/2)
        # i in the code stands for itteration
