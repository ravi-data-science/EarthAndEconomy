if __name__ == '__main__':

    dict1 = {"10":1,"20":2}
    lst1 = [2,3,4,6,7]

    for key,val in dict1.items():
        print(key)
        print(val)

    for val in enumerate(dict1):
        print(val)

    for i,v in enumerate(lst1):
        print(i)
        print(v)

        