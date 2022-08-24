"""
.py to collect base policies for this intro problem.
"""


class SellLow:
    """Class to implement the SellLow policy defined in the .pdf"""
    def __init__(self, model_type, theta_low, T):
        if model_type not in ['basic']:
            raise ValueError("Must use the basic model to implement this policy.")
        self.theta_low = theta_low
        self.T = T

    def think(self, S_t, t):
        """
        function to map from S_t --> x_t given SellLow policy.
        S_t : state of system at time t -- nd.array (2,)
        t : time step of system -- int
        """
        # If first case is met -- p_t < theta_low AND R_t = 1 (first parentheses)
        # If second case is met -- t = T (second parentheses)
        if (S_t[1] < self.theta_low and S_t[0] == 1) or (t == self.T and S_t[0] == 1):
            return 1
        else:
            return 0


class HighLow:
    """Class to implement the SellLow policy defined in the .pdf"""
    def __init__(self, model_type, theta_params, T):
        if model_type not in ['basic']:
            raise ValueError("Must use the basic model to implement this policy.")
        self.theta_low = theta_params[0]
        self.theta_high = theta_params[1]
        self.T = T

    def think(self, S_t, t):
        """
        function to map from S_t --> x_t given SellLow policy.
        S_t : state of system at time t -- nd.array (2,)
        t : time step of system -- int
        """
        # If first case is met -- p_t < theta_low AND p_t > theta_high
        # If second case is met -- t = T (second parentheses)
        if (S_t[1] < self.theta_low and S_t[1] > self.theta_high) or (t == self.T and S_t[0] == 1):
            return 1
        else:
            return 0