import numpy as np

robot_1_wins = 0
robot_2_wins = 0

for i in range(int(1e7)):
    while True:
        tot = np.random.uniform()
        if tot > 0.5:
            robot_1_wins += 1
            break
        tot -= np.random.uniform()
        if tot < -0.5:
            robot_2_wins += 1
            break

print("robot_1_wins = ", robot_1_wins)
print("robot_2_wins = ", robot_2_wins)
