#!/usr/bin/env python

import sys
import os
import Part4Mod

# Dictionary to represent a set of named variables we will use in our expressions
# Initially empty
#variables = { };
#variables['scale'] = 0.265
#variables['phi'] = 1.257
#variables['x'] = 16.3

#five = Part4Mod.RealValuedExpression(5.0)
#twenty = Part4Mod.RealValuedExpression(20.0)

# 
# STEP 2
#
# Rather than explicity construct a BinaryExpression we will leverage operator overlading
#twentyfive = five + twenty
#twentyfive_plus_phi = twentyfive + Part4Mod.VariableExpression('phi')

#print "%s -~-> %f" % (twentyfive, twentyfive.evaluate(variables),)
#print "%s -~-> %f\n" % (twentyfive_plus_phi, twentyfive_plus_phi.evaluate(variables),)

# 
# STEP 3
#
#scale_var = Part4Mod.VariableExpression('scale')
#phi_var = Part4Mod.VariableExpression('phi')
#x_var = Part4Mod.VariableExpression('x')

#sixty_scaled = twentyfive * scale_var
#x_over_phi = x_var / phi_var
#what = (sixty_scaled - x_over_phi) * (twentyfive_plus_phi + scale_var)

#print "%s -~-> %f" % (sixty_scaled, sixty_scaled.evaluate(variables),)
#print "%s -~-> %f" % (x_over_phi, x_over_phi.evaluate(variables),)
#print "%s -~-> %f\n" % (what, what.evaluate(variables),)

sys.exit(0)