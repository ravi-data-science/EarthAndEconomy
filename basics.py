from collections import deque

if __name__ == '__main__':
    # If statements don't need parentheses 
    # or curly braces.
    n = 1
    if n > 2:
        n -= 1
    elif n == 2:
        n *= 2
    else:
        n += 2

    print(n)
    # Parentheses needed for multi-line conditions.
    # and = &&
    # or  = ||
    n, m = 1, 2
    if ((n > 2 and 
        n != m) or n == m):
        n += 1

    print(n)
    print(m)    


    ####

    n = 5
    while n < 5:
        print(n)
        n += 1

    # Looping from i = 0 to i = 4
    for i in range(5):
        print(i)

    # Looping from i = 2 to i = 5
    for i in range(2, 6):
        print(i)

    # Looping from i = 5 to i = 2
    for i in range(5, 1, -1):
        print(i)

    #######
    # 
    print(float("inf"))
    print(10%3)

    ###
    arr = [2,3,4,5]
    arr.insert(6,7)
    print(arr)
    print(arr[1:3])
    print(arr[1:7]) # just gives entire list
    print()

    a,b,c = [1,2,3]
    print(a)
    print(b)
    print(c)

    arr_1 = [53,45,67] 
    for n in arr_1:
        print(n)

    for i,n in enumerate(arr_1):
        print(i) 
        print(n)   

    print("zip::")
    for n1,n2, in zip(arr,arr_1):
        print(n1)
        print(n2)    

    arr_3 = [i for i in range(4)]      
    print(arr_3)

    str_1 = ["ab","bc","cd"]
    print(",".join(str_1))
    
    ###
    q1 = deque()
    q1.append(1)
    q1.append(2)

    print("basic deque::")
    print(q1)
    q1.appendleft(3)
   
    print(q1)
    print(q1.popleft())
    print(q1.pop())

    # set
    set_1 = set()
    set_1.add(1)
    print(set_1)

    #map
    map_1 = {"ram":"raghav","ten":"command"}

    for key,value in map_1.items():
        print(key)
        print(value)
