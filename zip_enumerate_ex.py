
if __name__=="__main__":
    name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
    roll_no = [ 4, 1, 3, 2 ]

    # using zip() to map values
    mapped = zip(name, roll_no)
    print(mapped)

    print(set(mapped))