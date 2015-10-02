#!/usr/bin/env python

import sys
import os
import Part3Mod

# Dictionary to represent a set of named variables we will use in our expressions
# Initially empty
variables = { };

#
# STEP 1:
#

# Here is a simple example of some real values expressions
#five = Part3Mod.RealValuedExpression(5.0)
#twenty = Part3Mod.RealValuedExpression(20.0)

#print "five -~-> %f" % five.evaluate(variables)
#print "twenty -~-> %f\n" % twenty.evaluate(variables)

#
# STEP 2: Do not uncomment until STEP 1 is complete
#

# We can construct more complex expressions like five + twenty or five * 12:
#twentyfive = Part3Mod.BinaryExpression(five, twenty, '+')
#fivetimestwelve = Part3Mod.BinaryExpression(five, Part3Mod.RealValuedExpression(12.0), '*')
#thirtytyfive = Part3Mod.BinaryExpression(fivetimestwelve, twentyfive, '-')

# %s invokes the str() function on the argument to format
#print "%s -~-> %f" % (twentyfive, twentyfive.evaluate(variables),)
#print "%s -~-> %f" % (fivetimestwelve, fivetimestwelve.evaluate(variables),)
#print "%s -~-> %f\n" % (thirtytyfive, thirtytyfive.evaluate(variables),) 

#
# STEP 3: Do not uncomment until STEP 2 is complete
#

# Let introduce variables into the mix
#variables['scale'] = 0.265
#variables['phi'] = 1.257
#variables['x'] = 16.3

#scale_var = Part3Mod.VariableExpression('scale')
#phi_var = Part3Mod.VariableExpression('phi')
#x_var = Part3Mod.VariableExpression('x')

#sixty_scaled = Part3Mod.BinaryExpression(fivetimestwelve, scale_var, '*')
#x_over_phi = Part3Mod.BinaryExpression(x_var, phi_var, '/')

#print "%s -~-> %f" % (sixty_scaled, sixty_scaled.evaluate(variables),)
#print "%s -~-> %f\n" % (x_over_phi, x_over_phi.evaluate(variables),)

#
# STEP 4: Do not uncomment until STEP 3 is complete
#

# Optional: Making things really complicated...
#what1 = Part3Mod.BinaryExpression(sixty_scaled, x_over_phi, '-')
#what2 = Part3Mod.BinaryExpression(what1, what1, '+')

#print "%s -~-> %f\n" % (what2, what2.evaluate(variables),)

sys.exit(0)