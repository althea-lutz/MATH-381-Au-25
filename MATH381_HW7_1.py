import random

def ball_game(n, k, samplesize):

        samples = []

        for i in range(samplesize):
            t = 0
            balls = [k for _ in range(n)]
            while all(b > 0 for b in balls):
                t += 1
                player_i = random.randrange(n)
                player_j = random.randrange(n)
                while player_j == player_i:
                    player_j = random.randrange(n)
                balls[player_i] -= 1
                balls[player_j] += 1
            samples.append(t)

        expected_val = sum(samples) / len(samples)

        var = 0

        for t in set(samples):
            t_prob = samples.count(t) / len(samples)
            square_diff = (t - expected_val) ** 2
            var += t_prob * square_diff

        return var

print(ball_game(3, 6, 100000))



