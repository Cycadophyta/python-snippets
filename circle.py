import math

class Circle:
    
    '''Circle with radius, area and diameter.'''
    
    def __init__(self, radius=1):
        self.radius = radius
        
    def __repr__(self):
        return f'{self.__class__.__name__}({self.radius})'
        
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = value

    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError('Diameter cannot be negative')
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2
    

def printer():
    print(c)
    print('Radius =', c.radius)
    print('Diameter =', c.diameter)
    print('Area =', c.area)
    print()
    
c = Circle()
printer()

c.radius = 2
printer()

c.diameter = 12
printer()