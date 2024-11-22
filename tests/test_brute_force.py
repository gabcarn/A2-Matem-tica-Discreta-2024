import unittest
from algorithms import brute_force
from data.graphs import G_Crow, G_10_9_4, G_10_9_6

class IncompleteColoring(unittest.TestCase):
    def test_q_greather_than_chromatic(self):
        self.assertEqual(brute_force(G_10_9_4, 4, []), [0, 1, 2, 3, 0, 1, 0, 1, 0, 1])
        
    def test_q_equal_chromatic(self):
        self.assertEqual(brute_force(G_10_9_6, 6, [0, 0, 2, 3, 1, 5]), [0, 1, 2, 3, 4, 5, 0, 1, 0, 1])
     
    def test_q_less_than_chromatic(self):
        self.assertEqual(brute_force(G_Crow, 3, [0, 2, 1]), [])
    
    def test_q_greather_than_vertices(self):
         self.assertEqual(brute_force(G_10_9_4, 11, [0, 2, 7, 7, 3]), [])

class CompleteColoring(unittest.TestCase):
    def test_complete_coloring_invalid(self):
         self.assertEqual(brute_force(G_10_9_6, 6, [0, 1, 2, 3, 4, 5, 0, 0, 1, 1]), [0, 1, 2, 3, 4, 5, 0, 1, 0, 1])

    def test_complete_coloring_valid(self):
        self.assertEqual(brute_force(G_Crow, 6, [0, 1, 2, 3, 4, 5]), [0, 1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main(verbosity=2)