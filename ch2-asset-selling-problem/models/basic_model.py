"""
.py file to store work on the model for Asset Selling Problem.
"""
import numpy as np
from scipy.stats import norm


class AssetSellingModel:
    """
    Class to instantiate a model for the Asset selling problem described in 2.2 of
    https://castlelab.princeton.edu/wp-content/uploads/2022/01/Powell-Sequential-Decision-Analytics-Jan292022-2.pdf
    """
    def __init__(self, mu=0, sigma=1, seed_num=1):
        np.random.seed(seed_num)
        self.mu = mu
        self.sigma = sigma
        self.S_t = np.array([1, round(norm.ppf(np.random.random(), self.mu, self.sigma), 4)])
        self.done = False
        self.C_t = 0
        self.model_type = 'basic'
        self.t = 0


    def step(self, x_t):
        """
        x_t : action taken at time t in {0, 1}
        """
        if x_t not in [0, 1]:
            raise ValueError(f"{x_t} is not an allowable action; must be 0 or 1.")
        
        # Update according to S^M in basic-formulation.md
        self.S_t = np.array([
            self.S_t[0] - x_t, round(norm.ppf(np.random.random(), self.mu, self.sigma), 4)
        ])

        # Update contribution function earnings += x_t * p_t.
        self.C_t += x_t * self.S_t[1]

        # Update timestep.
        self.t += 1
