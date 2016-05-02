#!/usr/bin/env python3

import unittest
from Hebbian import HebbianRule

class TestHebbianRule(unittest.TestCase):
    def setUp(self):
        self.hebbian_rule = HebbianRule()
    
        
    def tearDown(self):
        del self.hebbian_rule
        
    
    def test_set_learning_rate(self):
        rate = 0.01
        self.hebbian_rule.set_learning_rate(rate)
        self.assertEqual(rate, self.hebbian_rule.learning_rate)
    
    def test_new_weight(self):
        old_weight = 0.5
        input_value = 1
        output_value = 1
        new_weight = self.hebbian_rule.new_weight(old_weight, input_value, output_value)
        self.assertGreater(new_weight, old_weight)
