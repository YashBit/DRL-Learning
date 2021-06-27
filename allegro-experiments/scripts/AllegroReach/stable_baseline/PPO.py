
import gym
import  allegro_gym
import os 
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env

"""
TODO:

1A. MAKE SURE THAT THE MODEL TAKES IN THE CORRECT INPUT
1B. Make sure that the policy is training correctly
1C: Make sure that the model.save is in the correct place
1D: Make sure that the observation type is correct 


SBATCH FILE 

#You need to print it in the file in this python file

2. Saving the logs in the correct folder - DONE
3. Saving the model in the correct folder - DONE


TESTING:
4. Setting the correct tensorboard links


ALGORITHMS:

5. A2C ,DDPG, DQN, HER, SAC, TD3


FINAL REQUESTS:

6. 7 Hr Requests: 5M Steps



"""

#Load the environment

# SPARSE REWARDS -> AllegroReachDense-v0

# env = gym.make('AllegroReach-v0')
# env = DummyVecEnv([lambda:env])


env = make_vec_env("CartPole-v1", n_envs=4)

"""

PRINTING THE MATERIAL

"""

print("CARTPOLE")
print(env.observation_space)
print(env.action_space)








#Training the model

model = PPO('MlpPolicy', env, verbose = 1, tensorboard_log = "/home/yb1025/Research/PintoLab/allegro-gym/stable_baselines/reach/logs/")

#Model, #of TimeSteps: 5000000
model.learn(total_timesteps = 5000000)

#Saving the model:

model.save("ppo_reach")


#Deleting the model

del model

#RELOAD ANOTHER MODEL ANOTHER MODEL
model = PPO.load("ppo_reach")

#Evaluate the Policy


#Is this the correct way to call the evaluate policy will it be printed?
evaluate_policy(model, env, n_eval_episodes=10, render=True)

#You need to print the evaluate policy
# vim ~/.bashrc
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/yb1025/.mujoco/mujoco200/bin

#Testing the model. 

episodes = 20
for episode in range(1, episodes+1):
    obs = env.reset()
    done = False
    score = 0
    while not done:
        env.render()
        action, _states = model.predict(obs)
        obs, reward, dones, info = env.step(action)
        score += reward
        env.render()
        
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




