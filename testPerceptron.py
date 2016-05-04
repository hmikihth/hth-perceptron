#!/usr/bin/env python3

import unittest
from inspect import isfunction
from Perceptron import Perceptron

def myfunc(summa):
    if summa == 6:
        return True
    return False

class TestPerceptron(unittest.TestCase):
    def setUp(self):
        self.perceptron = Perceptron()
    
    
    def tearDown(self):
        del self.perceptron
    

    def test_setAllInputs(self):
        values = [0,1,0]
        self.perceptron.setAllInputs(values)
        self.assertEqual(self.perceptron.inputs, values)


    def test_setInput(self):
        self.perceptron.setAllInputs([0,0,0])
        n = 1
        value = 1
        self.perceptron.setInput(n, value)
        self.assertEqual(self.perceptron.inputs[n], value)
    
        
    def test_setAllWeights(self):
        values = [0,1,0]
        self.perceptron.setAllWeights(values)
        self.assertEqual(self.perceptron.weights, values)


    def test_setWeight(self):
        self.perceptron.setAllWeights([0,0,0])
        n = 1
        value = 1
        self.perceptron.setWeight(n, value)
        self.assertEqual(self.perceptron.weights[n], value)
        
        
    def test_setFunc(self):
        self.perceptron.setFunc(myfunc)
        self.assertTrue(isfunction(self.perceptron.func))
        
        
    def test_calculate(self):
        self.perceptron.setAllInputs([1,1,1])
        self.perceptron.setAllWeights([1,2,3])
        self.perceptron.setFunc(myfunc)
        self.perceptron.calculate()
        self.assertTrue(self.perceptron.output)

         
    def test_get(self):
            
        self.perceptron.setAllInputs([1,1,1])
        self.perceptron.setAllWeights([1,2,3])
        self.perceptron.setFunc(myfunc)
        self.perceptron.calculate()
        self.assertTrue(self.perceptron.get())

        self.perceptron.setAllWeights([1,2,4])
        self.perceptron.calculate()
        self.assertFalse(self.perceptron.get())
