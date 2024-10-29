
if __name__=='__main__':
    a = [1, 3, 5, 7, 9]

    # On each iteration val
    # represents the current item/element
    for val in a:
        print(val)

    # Calculate the length of the list
    n = len(a)
    
    # Iterates over the indices from 0 to n-1 (i.e., 0 to 4)
    for i in range(n):
        print(a[i])

    # Start from the first index
    i = 0
    
    # The loop runs till the last index (i.e., 4)
    while i < len(a):
        print(a[i])
        i += 1    

    # Here, i and val reprsents index and value respectively
    for i, val in enumerate(a):
        print (i, val)    

    # On each iteration val is passed to print function
    # And printed in the console.
    [print(val) for val in a]   