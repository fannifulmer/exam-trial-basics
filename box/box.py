# Create a class that represents a cuboid:
# It should take its three dimensions as constructor parameters (numbers)
# It should have a method called `get_surface` that returns the cuboid's surface
# It should have a method called `get_volume` that returns the cuboid's volume

class Cuboid(object):
    def __init__(self, aside = 10, bside = 20, cside = 30):
        pass
    
    def get_surface(self):
        pass
    
    def get_volume(self):
        pass

box = Cuboid(10, 20, 30)
print(box.get_surface()) # should print 2200
print(box.get_volume()) # should print 6000
