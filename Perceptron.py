#!/usr/bin/env python3

from inspect import isfunction

class Perceptron():
    def __init__(self):
        pass
        
    
    def setInput(self, n, value):
        pass
        
    
    def setAllInput(self, values):
        pass
        
        
    def setWeight(self, n, weight):
        pass
        
        
    def setFunc(self, func):
        if isfunction(func):
            self.func = func
        
        
    def calculate(self):
        pass
        
        
    def get(self):
        sum = self.calculate()
        return self.func(sum)
