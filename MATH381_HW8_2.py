import numpy as np

# Simulates a Metropolis chain to estimate the number
# of balls each player has in a game where at each step,
# player i gives 1 ball to player j, with
# distribution proportional to the product of the numbers of balls each player has.

def ball_game(n, k, sample_size = 1000000, burn = 1000000):

    # A state is stored as a length n list, where an
    # entry is within the range [0, k], denoting
    # how many balls a player has.

    # Initial state
    state = np.full(n, k, dtype=int)

    # Burn-in stage
    for t in range(burn):
        step(state)

    # For each step after the burn-in period,
    # record the samples of the final state.
    samples = []
    for t in range(sample_size):
        step(state)
        f = 1
        for s in range(len(state)):
            f = f * state[s]
        samples.append(f)

    # Return the average of the function F
    return sum(samples) / len(samples)

# Performs a step of the Metropolis chain.
def step(state):

    n = len(state)

    # Choose 2 random players
    pi, pj = np.random.choice(n, 2)

    # Use the proposal chain to propose a new state.
    # The state only changes at the indices pi and pj,
    # so only store those for efficiency.
    while pi == pj:
        pj = np.random.choice(n)
    proposal_pi = state[pi] - 1
    proposal_pj = state[pj] + 1

    # Decide whether to accept the proposal.
    alpha = (proposal_pi * proposal_pj) / (state[pi] * state[pj])
    r = np.random.rand()
    if r < alpha:
        state[pi] = proposal_pi
        state[pj] = proposal_pj

    return

print(ball_game(4,5))


