#! /usr/local/bin/python3.4
from math import sqrt

__author__ = 'ee364e10'

class Point3D:
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self , x= 0.0 , y = 0.0 , z= 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return ("{0:0.2f} , {1:0.2f} , {2:0.2f}".format(self.x,self.y,self.z))

    def distFrom(self,other):
        dist = 0
        dist = ((self.x - other.x)**2)+((self.y - other.y)**2)+ ((self.z - other.z)**2)
        return sqrt(dist)

    def nearestPoint(self,points):
        if not points:
            return None

        min = self.distFrom(points[0])
        j = points[0]
        for i in points:
            if ( self.distFrom(i) < min):
                min = self.distFrom(points[1])
                j = i
        return j


    def clone(self):
        return Point3D(self.x , self.y , self.z)

    def __add__(self, other):
        if isinstance(other,float):
            return Point3D(self.x+other , self.y+other , self.z+other)
        elif isinstance(other,self.__class__):
            return Point3D(self.x+other.x , self.y+other.y , self.z+other.z)
        else:
           print("PLEASE ENTER FLOAT VALUES AS SAID IN THE PRELAD DOCUMENT")
    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other,float):
            return Point3D(self.x-other , self.y-other , self.z-other)
        elif isinstance(other,self.__class__):
            return Point3D(self.x-other.x , self.y-other.y , self.z-other.z)
        else:
           print("PLEASE ENTER FLOAT VALUES AS SAID IN THE PRELAD DOCUMENT")
    def __neg__(self):
        return Point3D(self.x * -1 ,self.z * -1, self.y * -1 )

    def __div__(self, other):
        if isinstance(other,float):
            return Point3D(self.x/other , self.y/other , self.z/other)
        else:
           print("PLEASE ENTER FLOAT VALUES AS SAID IN THE PRELAD DOCUMENT")
    def __mul__(self, other):
       if isinstance(other,float):
            return Point3D(self.x*other , self.y*other , self.z*other)
       else:
           print("PLEASE ENTER FLOAT VALUES AS SAID IN THE PRELAB DOCUMENT")
    __rmul__ = __mul__

    def __eq__(self, other):
        if ( self.x == other.x ) & (self.y == other.y ) & (self.z == other.z):
            return True
        else:
            return False

    def __gt__(self, other):
        if ( self.x > other.x ) & (self.y > other.y ) & (self.z > other.z):
            return True
        else:
            return False

    def __ge__(self, other):
        if ( self.x >= other.x ) & (self.y >= other.y ) & (self.z >= other.z):
            return True
        else:
            return False

    def __lt__(self, other):
        if ( self.x < other.x ) & (self.y < other.y ) & (self.z < other.z):
            return True
        else:
            return False

    def __le__(self, other):
        if ( self.x <= other.x ) & (self.y <= other.y ) & (self.z <= other.z):
            return True
        else:
            return False

    def __hash__(self):
        pointTuple = self.x, self.y, self.z
        return hash(pointTuple)

class PointSet:
    points = set([])

    def __init__(self , points = set()):
        self.seT = points

    def addPoint(self , p):
        self.points.add(p)

    def count(self):
        return (len(self.points))

    def computeBoundingBox(self):
        a = self.points.pop()
        min_x = max_x = a.x
        min_y = max_y = a.y
        min_z = max_z = a.z
        self.points.add(a)
        tup = 0
        for i in self.points:
            min_x = min( i.x , min_x)
            min_y = min( i.y , min_y)
            min_z = min( i.z , min_z)

            max_x = max( i.x , max_x)
            max_y = max( i.y , max_y)
            max_z = max( i.z , max_z)
        A = Point3D(min_x,min_y, min_z)
        B = Point3D(max_x, max_y, max_z)
        list = [A , B]
        tup = tuple(list)
        return tup

    def computeNearestNeighbors(self , other):
        list = []
        for i in self.points:
            tup = (i)
            distance = 0
            for oppa in other.points:
                if distance > i.distFrom(oppa ):
                    distance = i.distFrom(oppa)
            tup.add(oppa)
            list.append(tup)
        return list

    def __add__(self, point):
        n = PointSet(self)
        n.add(point)
        return n

    def __add__(self, other):
        n = PointSet(self)
        i = PointSet(other)
        return n.append(i)

    def __sub__(self, other):
        n = self.points + other.points
        for i in self.points:
            for j in other.points:
                if i is j:
                    print("same")
                    n.remove(j)
        return n

    def __sub__(self, point):
        return self.points.remove(point)

    def __gt__(self, other):
        if self.points.count() > other.pointscount ():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.points.count() >= other.pointscount ():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.points.count() < other.pointscount ():
            return True
        else:
            return False

    def __le__(self, other):
        if self.points.count() <= other.pointscount ():
            return True
        else:
            return False

if __name__ == "__main__":
    print ('Hello')
    # print(Point3D(3.99 ,2.55,4.88 ))
    # a = [Point3D(0,0,1 ), Point3D(3,3,3 ) , Point3D(2,2,2)]
    # print('Hello')
    # print(Point3D(0,0,0).nearestPoint(a))
    a = set([])
    PointSet(a).addPoint(Point3D(1,1,1))
    PointSet(a).addPoint(Point3D(1,2,1))
    PointSet(a).addPoint(Point3D(1,3,1))
    b = set([])
    PointSet(b).addPoint(Point3D(1,1,1))
    PointSet(b).addPoint(Point3D(1,2,0))
    PointSet(b).addPoint(Point3D(1,3,0))

    print(b)