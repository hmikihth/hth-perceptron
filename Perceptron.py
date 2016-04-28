#!/usr/bin/env python3

from inspect import isfunction

class Perceptron():
    def __init__(self):
        pass
        
    
    def setInput(self, n, value):
        self.inputs[n] = value
        
    
    def setAllInputs(self, values):
        self.inputs = values
        
        
    def setWeight(self, n, weight):
        self.weights[n] = weight


    def setAllWeights(self, weights):
        self.weights = weights
        
        
    def setFunc(self, func):
        if isfunction(func):
            self.func = func
        
        
    def calculate(self):
        summa = 0
        n = 0
        for i in self.inputs:
            summa += i * self.weights[n]
            n += 1
        return summa
        
    def get(self):
        summa = self.calculate()
        return self.func(summa)
