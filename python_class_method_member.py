class Person:

    def __init__(self, i2):
        self.i2 = i2
        print("from init::"+self.i2)

    
    def m1(self,i1:int):
        self.i1 = i1
        print("i1 int::"+str(self.i1))
        print(self.i2)

if __name__=='__main__':
    p1 = Person('i2 string')   
    print(p1.m1(20))     