# Create a class that represents a cuboid:
# It should take its three dimensions as constructor parameters (numbers)
# It should have a method called `get_surface` that returns the cuboid's surface
# It should have a method called `get_volume` that returns the cuboid's volume

class Cuboid(object):
    def __init__(self, h = 10, w = 20, l = 30):
        self.h = h 
        self.w = w 
        self.l = l
    
    def get_surface(self):
        return(2 * (self.l*self.w + self.w*self.h + self.h*self.l))
    
    def get_volume(self):
        return(self.l * self.w * self.h)

box = Cuboid(10, 20, 30)
print(box.get_surface()) # should print 2200
print(box.get_volume()) # should print 6000
