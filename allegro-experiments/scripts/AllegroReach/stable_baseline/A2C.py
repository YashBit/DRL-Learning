
import gym
import allegro_gym
import os 
import gym
from stable_baselines3 import A2C
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy





"""
TODO:
1. Make sure that the policy is training correctly


SBATCH FILE 
2. Saving the logs in the correct folder
3. Saving the model in the correct folder


TESTING:
4. Setting the correct tensorboard links


ALGORITHMS:

5. A2C, DDPG, DQN, HER, PPO, SAC, TD3


FINAL REQUESTS:

6. 7 Hr Requests: 5M Steps



"""












#Load the environment
env = gym.make('AllegroReach-v0')
env.reset()


#Training the model

model = PPO('MlpPolicy', env, verbose = 1, tensorboard_log = log_path)

#Model, #of TimeSteps: 5000000
model.learn(total_timesteps = 5000000)

#Saving the model:

model.save(pathVariable)


#Deleting the model

del model

#RELOAD ANOTHER MODEL ANOTHER MODEL
model = PPO.load(PPO_path, env = env)

evaluate_policy(model, env, n_eval_episodes=10, render=True)


#Testing the model. 

episodes = 20
for episode in range(1, episodes+1):
    obs = env.reset()
    done = False
    score = 0
    while not done:
        env.render()
        action = model.predict(obs)
        obs, reward, done, info = env.step(action)
        score += reward
        
    print('Episode: {} Score: {}'.format(episode, score))

# for i in range(100000):
#     action = env.action_space.sample()*0.
#     action[:3] = 1.0
#     action[3:6] = 0.1
#     action[6:9] = 0.01
#     obs, reward, done, info = env.step(action)
#     env.render()
#     print(env.sim.get_state().qpos)
#     if(info['is_success']):
#         print("Reached goal!")
#     if i%100==0:
#         print("Resetting")
#         env.reset()




