#! /usr/bin/env python

import sys
import os
import math
import Part2Mod

# The standard argument checks
if len(sys.argv) != 3:
	sys.stderr.write("usgae: Part2.py <point file 1> <point file 2>\n")
	sys.exit(1)

if not os.path.isfile(sys.argv[1]) or not os.access(sys.argv[1], os.R_OK):
	sys.stderr.write("error: %s is not a readable file.\n" % (sys.argv[1],))
	sys.exit(2)
	
if not os.path.isfile(sys.argv[2]) or not os.access(sys.argv[2], os.R_OK):
	sys.stderr.write("error: %s is not a readable file.\n" % (sys.argv[2],))
	sys.exit(3)
	
# Create two point sets
pointset1 = Part2Mod.PointSet()
pointset2 = Part2Mod.PointSet()

# Read in point set 1:
fp = open(sys.argv[1], "r")
for line in fp:
	# Contruct a new Point3D object and add it to the point set
	line = line.split(",")
	p = Part2Mod.Point3D(float(line[0]), float(line[1]), float(line[2]))
	pointset1.add_point(p)
fp.close()

# Read in point set 2:
fp = open(sys.argv[2], "r")
for line in fp:
	line = line.split(",")
	p = Part2Mod.Point3D(float(line[0]), float(line[1]), float(line[2]))
	pointset2.add_point(p)
fp.close()

# Get the bounding boxes and neareast neighbors
min1, max1 = pointset1.compute_bounding_box()
min2, max2 = pointset2.compute_bounding_box()
nearest_neighbors = pointset1.compute_nearest_neighbors(pointset2)

print "Point Set 1"
print "  Number of points: %d" % (pointset1.get_num_points())
print "  Bounding Box: min: %s max: %s" % (min1, max1)
print
print "Point Set 2"
print "  Number of points: %d" % (pointset2.get_num_points())
print "  Bounding Box: min %s max %s" % (min2, max2)
print
print "Nearest Neighbors"
for pair in nearest_neighbors:
	print "%s is closest to %s" % (pair[0], pair[1])
	
sys.exit(0)

