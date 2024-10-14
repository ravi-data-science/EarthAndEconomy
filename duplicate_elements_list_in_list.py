
from typing import List

def d1(lst1: List[int]) -> map:
    # print(lst1)
    map1 = {}

    for i,v in enumerate(lst1):
        # print(i)
        # print(v)

        if v in map1:
            map1[v] += 1
        else:
            map1[v] = 1
    return map1        



if __name__ == '__main__':

    lst1 = [1,2,1,3,4,5,4,3,2]
    hashmap1 = d1(lst1)
    print(hashmap1)
    # Sample dictionary
    # data = {'a': 10, 'b': 25, 'c': 5, 'd': 30}

    # Lambda function to select elements where value > 10
    filtered_data = dict(filter(lambda item: item[1] > 10, hashmap1.items()))

    # Output the filtered dictionary
    print(filtered_data)
