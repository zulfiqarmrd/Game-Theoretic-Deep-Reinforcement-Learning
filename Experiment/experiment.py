import sys
sys.path.append(r"/home/neardws/Documents/Game-Theoretic-Deep-Reinforcement-Learning/")
from absl import app
from Experiment import run_mad4pg
from Experiment import run_ddpg
from Experiment import run_mpo
from Experiment import run_ra

if __name__ == '__main__':
    app.run(run_mad4pg.main)
    # app.run(run_mpo.main)