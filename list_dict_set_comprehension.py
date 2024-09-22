from collections import deque

if __name__ == '__main__':

    names = ['kai', 'abe', 'ada', 'gus', 'zoe']
    upper_names = [name.upper() for name in names]
    print(upper_names)


    # Start with an empty list.
    users = []
    # Make a new user, and add them to the list.
    new_user = {
    'last': 'fermi',
    'first': 'enrico',
    'username': 'efermi',
    }
    users.append(new_user)
    # Make another new user, and add them as well.
    new_user = {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie',
    }
    users.append(new_user)
    # Show all information about each user.
    for user_dict in users:
        for k, v in user_dict.items():
            print(k + ": " + v)
            print("\n") 

    ####

    #lists in dict
    # Store multiple languages for each person.
    fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
    # Show all responses for each person.
    for name, langs in fav_languages.items():
        print(name + ": ")
        for lang in langs:
            print("- " + lang)        


    from collections import OrderedDict
    # Store each person's languages, keeping
    # track of who respoded first.
    fav_languages = OrderedDict()
    fav_languages['jen'] = ['python', 'ruby']
    fav_languages['sarah'] = ['c']
    fav_languages['edward'] = ['ruby', 'go']
    fav_languages['phil'] = ['python', 'haskell']
    # Display the results, in the same order they
    # were entered.
    for name, langs in fav_languages.items():
        print(name + ":")
    for lang in langs:
        print("- " + lang)        


   # dict comprehensiion

   # Python code to demonstrate dictionary 
# comprehension

    # Lists to represent keys and values
    keys = ['a','b','c','d','e']
    values = [1,2,3,4,5]  

    # but this line shows dict comprehension here  
    myDict = { k:v for (k,v) in zip(keys, values)}  

    # We can use below too
    # myDict = dict(zip(keys, values))  

    print (myDict)     

    dic=dict.fromkeys(range(5), True)

    print(dic)


    ##
    myDict = {x: x**2 for x in [1,2,3,4,5]}
    print (myDict)


    sDict = {x.upper(): x*3 for x in 'coding '}
    print (sDict)

    r_dict = {x:x+1 for x in range(1,10)}

    print(r_dict)
