class Rectangle:
    def set_dim(self, l, b):
        self.l = l
        self.b = b 
    def area(self):
        return self.l*self.b
    
    
    
    
n = int(input("Enter Number of Reactangle:"))
shape = []
for i in range(n):
    r= Rectangle()
    l = int(input("Enter Length of rectangle {}".format(i+1)"))
    b = int(input("Enter the breadth of reactangle{}". format{i+1}))
    r.set_dim(l,b)
    shape.append(r)
        
index = 0 
for i in shape:
    index = index +1
    res = i.area()
    print("Area {} is {}".format(index, res))

