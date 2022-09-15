import numpy as np

season = int(input("how many seasons? (only integer numbers are valid)"))
episode = int(input("how many episodes? (only integer numbers are valid)"))

season_list = np.arange(season)
episode_list = np.arange(episode)

print("Season = {}".format(np.random.choice(season_list) + 1))
print("Episode = {}".format(np.random.choice(episode_list) + 1))
