#! /usr/bin/env python

import sys
import os

class Expression:
	def __init__(self):
		# Function: Constructs a new expression
		pass
	
	def evaluate(self, variables):
		# Function: Evaluates the expression and returns the real valued result of the expression (e.g. 5.5 + 2 evaluates to 7.5)
		# Arguments: 
		# 1. variables - A dictionary mapping variable names to real values
		pass
		
	def __str__(self):
		# Functions: (Special) Returns a string representation of this expression
		# This function is called when the object is passes to the str() function
		return ""
		
class RealValuedExpression(Expression):
	def __init__(self, value):
		pass
		
	def evaluate(self, variables):
		pass
		
	def __str__(self):
		pass

class BinaryExpression(Expression):
	def __init__(self, lhs, rhs, op):
		pass

	def evaluate(self, variables):
		pass

	def __str__(self):
		pass

class VariableExpression(Expression):
	def __init__(self, variable_name):
		pass
	
	def evaluate(self, variables):
		pass
			
	def __str__(self):
		pass
		