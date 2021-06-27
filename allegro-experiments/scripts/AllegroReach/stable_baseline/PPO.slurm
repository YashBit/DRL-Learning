#!/bin/bash
#SBATCH --job-name=PPO_search
#SBATCH --open-mode=append
#SBATCH --output=/home/yb1025/Research/PintoLab/allegro-gym/stable_baselines/reach/logs/PPO.out
#SBATCH --error=/home/yb1025/Research/PintoLab/allegro-gym/stable_baselines/reach/logs/PPO.err
#SBATCH --export=ALL
#SBATCH --time=7:00:00
#SBATCH --gres=gpu:1
#SBATCH --mem=64G
#SBATCH -c 4

## TODO: Run your hyperparameter search in a singularity container. Remember to 
## activate your Conda environment in the container before running your Python script.
singularity exec --bind /home/yb1025/mj_envs/mujocopy-buildlock:/ext3/miniconda3/lib/python3.8/site-packages/mujoco_py/generated/mujocopy-buildlock --overlay /home/yb1025/mj_envs/overlay-7.5GB-300K.ext3:ro /scratch/work/public/singularity/cuda11.1.1-cudnn8-devel-ubuntu20.04.sif /bin/bash -c "
source /ext3/env.sh
export LD_PRELOAD=/share/apps/local/lib/libGL.so
export OMP_NUM_THREADS=1
source activate allegro_gym
python PPO.py
"

