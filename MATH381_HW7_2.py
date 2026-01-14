import random
import numpy as np
import matplotlib.pyplot as plt

def ball_game(n, k, samplesize):

    samples = []
    prob_p1_loses = 0

    for i in range(samplesize):
        t = 0
        balls = [1 for _ in range(n)]
        balls[0] = k
        while all(b > 0 for b in balls):
            t += 1
            player_i = random.randrange(n)
            player_j = random.randrange(n)
            while player_i == player_j:
                player_j = random.randrange(n)
            balls[player_i] -= 1
            balls[player_j] += 1
        samples.append(t)
        if balls[0] == 0:
            prob_p1_loses += 1
    prob_p1_loses = prob_p1_loses / len(samples)

    return prob_p1_loses

for i in range(6):
    print(f"k = {i} → {ball_game(3, i, 1000000)}")

x_vals = np.array([1, 10, 20, 15, 20, 30])
y_vals = np.zeros(x_vals.size)

for i in range(x_vals.size):
    y_vals[i] = ball_game(4, x_vals[i], 3000000)

def powregression(x, y, plot=True):
    log_x = np.log(x)
    log_y = np.log(y)
    a, b = np.polyfit(log_x,log_y,1)

    if plot:
        line = [a*x0 + b for x0 in log_x]
        plt.scatter(log_x,log_y)
        plt.plot(log_x,line)
        plt.show()

    print(a, np.exp(b))
    return a, np.exp(b)

powregression(x_vals, y_vals)

