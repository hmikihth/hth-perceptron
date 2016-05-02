#!/usr/bin/env python3

from Perceptron import Perceptron

class PerceptronNetwork():
    def __init__(self):
        pass


    def set_retina(self, retina):
        self.retina = retina
        
        
    def set_number_of_hidden_layers(self, value):
        self.number_of_hidden_layers = value


    def set_number_of_outputs(self, value)
        self.number_of_outputs = value
        
        
    def create_network(self):
        self.layers = []
        for n in range(self.number_of_hidden_layers):
            layer = []
            for m in range(self.retina.size):
                layer.append(Perceptron())
            self.layers.append(layer)
        layer = []
        for n in range(self.number_of_outputs):
            layer.append(Perceptron())
        self.layers.append(layer)
        
        
    def get_output(self):
        pass
    
    
    def teach(self):
        pass
