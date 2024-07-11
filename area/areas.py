class Cirlcle:
    def __init__(self,radius):
        self.radius = radius
        self.pi = 3.14
    def area(self):
        
        area = 2*self.pi*self.radius
        return area
    def circumfrence (self):
        pi = 3.14
        circumfrence = round(self.pi *self.radius**2,2)
        return circumfrence
    
area = Cirlcle(3.1)
cicumfrence = Cirlcle(123.1)
print (area.area())
print (area.circumfrence())
