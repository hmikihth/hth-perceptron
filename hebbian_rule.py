#!/usr/bin/env python3


class HebbianRule():
    def __init__(self, learning_rate=0.1):
        self.set_learning_rate(learning_rate)
        
    
    def set_learning_rate(self, learning_rate):
        self.learning_rate = learning_rate
        
        
    def new_weight(old_weight, input_value, output_value):
        return old_weight + self.learning_rate * input_value * output_value
