#!/usr/bin/env python3

import unittest
from inspect import isfunction
from Perceptron import Perceptron


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
        def myfunc():
            pass
            
        self.perceptron.setFunc(myfunc)
        self.assertTrue(isfunction(self.perceptron.func))
        
        
    def test_calculate(self):
        self.perceptron.setAllInputs([1,1,1])
        self.perceptron.setAllWeights([1,2,3])
        summa = self.perceptron.calculate()
        self.assertEqual(summa, 6)

         
    def test_get(self):
        def myfunc(summa):
            if summa == 6:
                return True
            return False
            
        self.perceptron.setAllInputs([1,1,1])
        self.perceptron.setAllWeights([1,2,3])
        summa = self.perceptron.calculate()
        self.perceptron.setFunc(myfunc)
        self.assertTrue(self.perceptron.get())

        self.perceptron.setAllWeights([1,2,4])
        summa = self.perceptron.calculate()
        self.assertFalse(self.perceptron.get())
