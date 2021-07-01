def theta_policy(obs):
    theta = obs[2]
    return 0 if theta < 0 else 1

import gym
env = gym.make('CartPole-v1')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        action = theta_policy(observation)
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()