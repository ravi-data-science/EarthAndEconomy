class MyClass1:
    def __init__(self):
        print("in init")
    def m1(self, i1:int):
        print(i1)    
    
  # A Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


 


if __name__=='__main__':
    print("in main")

    cla1 = MyClass1()
    #print(cla1)
    #print(cla1.m1(20))

    p = Person('Nikhil')
    p.say_hi() 