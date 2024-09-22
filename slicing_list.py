if __name__ == '__main__':

    finishers = ['sam', 'bob', 'ada', 'bea']
    first_two = finishers[:2]
    print(first_two)

    tuple_1 = ("1",1)
    print(tuple_1)


    fav_numbers = {'eric': 17, 'ever': 4}
    for name, number in fav_numbers.items():
        print(name + ' loves ' + str(number))


    fav_numbers = {'eric': 17, 'ever': 4}
    for name in fav_numbers.keys():
        print(name + ' loves a number')

    fav_numbers = {'eric': 17, 'ever': 4}
    for number in fav_numbers.values():
        print(str(number) + ' is a favorite')    

    name = input("What's your name? ")
    print("Hello, " + name + "!")

    age = input("How old are you? ")
    age = int(age)
    pi = input("What's the value of pi? ")
    pi = float(pi)


    class Dog():
        """Represent a dog."""
        def __init__(self, name):
            """Initialize dog object."""
            self.name = name
        def sit(self):
            """Simulate sitting."""
            print(self.name + " is sitting.")
        my_dog = Dog('Peso')
        print(my_dog.name + " is a great dog!")
        my_dog.sit()


    filename = 'siddhartha.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            print(line)    
      