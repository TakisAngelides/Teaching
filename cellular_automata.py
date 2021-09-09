import numpy as np
import random as rdm
import matplotlib.pyplot as plt

# The spins live on a line from 0 to N-1 and interact with nearest neighbours, the y axis is the time, they take values
# of 0 dead and 1 alive

N = 1001
T = 1001
# state_0 = [rdm.randint(0, 1) for _ in range(N)]
# state_0 = [1]*N
# state_0 = [1 if rdm.uniform(0, 1) > 0.1 else 0 for _ in range(N)]
state_0 = []
for i in range(N):
    if i == N//2:  # Double line casts to int automatically
        state_0.append(0)
    else:
        state_0.append(1)

states = [state_0]


def get_neighbours(i):

    if i == 0:

        current = i
        left = -1
        right = 1

    elif i == N - 1:

        current = i
        left = N - 2
        right = 0

    else:

        current = i
        left = i - 1
        right = i + 1

    return current, left, right


def evolve(T):

    for t in range(T):

        current_state = states[t]
        next_state = current_state.copy()  # This starts as a copy of current_state but will get mutated below

        for i in range(N):

            current, left, right = get_neighbours(i)

            if current_state[current] and current_state[left] and current_state[right]:

                next_state[current] = 0

            elif not current_state[current] and current_state[left] and not current_state[right]:

                next_state[current] = 1

            elif current_state[current] and not current_state[left] and not current_state[right]:

                next_state[current] = 0

            elif not current_state[current] and not current_state[left] and not current_state[right]:

                next_state[current] = 1

        states.append(next_state)


evolve(T)
plt.imshow(states, cmap='Greys',  interpolation='nearest')
plt.show()
