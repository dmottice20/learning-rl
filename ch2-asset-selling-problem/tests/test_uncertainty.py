"""
script to double check our uncertainty gen matches Table 2.1.
"""
import pytest
import numpy as np
from scipy.stats import norm


def test_random_vars():
    """
    Matching Table 2.1 in text.
    """
    U = np.array([
        0.8287, 0.6257, 0.9343, 0.4879, 0.3736,
        0.8145, 0.0385, 0.0089, 0.9430, 0.3693
    ])
    expected = np.array([
        0.949, 0.3206, 1.5086, -0.0303, -0.3223,
        0.8947, -1.7685, -2.3698, 1.5808, -0.3336
    ])
    actual = np.round(norm.ppf(U, 0, 1), decimals=4)
    assert np.array_equal(actual, expected), "Need the random gen to match Table 2.1"