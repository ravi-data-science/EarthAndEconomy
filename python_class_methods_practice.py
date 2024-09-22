from ast import Constant


class MyClass:



    def __init__(self, name):
            """Initialize dog object."""
            self.name = name
    def sit(self):
            """Simulate sitting."""
            print(self.name + " is sitting.")
    def f1():
        print ("in f1:")

    def f2(p1:str) -> str:
        print("in f2:"+p1)

if __name__=='__main__':
    
   print("in main")

   d1 = MyClass('dog1')

   print(d1.f2)
