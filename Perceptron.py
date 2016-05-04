#!/usr/bin/env python3

from inspect import isfunction

class Perceptron():
    def __init__(self):
        self.inputs = []
        self.weights = []
        
    
    def setAllInputs(self, values):
        self.inputs = values
        
        
    def setInput(self, n, value):
        self.inputs[n] = value
        
    
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
        self.output = self.func(summa)
        return summa
        
    def get(self):
        return self.output
