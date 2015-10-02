#! /usr/bin/env python

import sys
import os
import math

class Point3D:
	def __init__(self, x=0.0, y=0.0, z=0.0):
		# Put code here
		
	def distance_from(self, other):
		# Put code here
		# See http://en.wikipedia.org/wiki/Euclidean_distance for details...
		
	def nearest_point(self, points):
		# Put code here
		
	def clone(self):
		# Put code here
		
	def __str__(self):
		# Converts this object to a string representation
		# Called when you convert this object to a string with str()
		return "(%.3f, %.3f, %.3f)" % (self.x, self.y, self.z)
				
class PointSet:
	def __init__(self):
		# Put code here
		
	def add_point(self, p):
		# Put code here
		
	def get_num_points(self):
		# Put code here
		
	def compute_bounding_box(self):
		# Put code here
		
	def compute_nearest_neighbors(self, other_point_set):
		# Put code here
			
	
				