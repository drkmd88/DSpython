import unittest
import numpy as np
from src.similarity import *

class TestSim(unittest.TestCase):
    def test_sim(self):
        a = np.array([1,1])
        b = np.array([1,1])
        expect = 1
        actual = round(similarity(a,b),2)
        self.assertEqual(actual,expect)


if __name__ == '__main__':
    unittest.main()
