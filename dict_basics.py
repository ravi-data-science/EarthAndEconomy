from collections import deque

if __name__ == '__main__':
   dict_1 = {"ravi":20,"ram":40} 
   for k,v in dict_1.items():
     print(k)
     print(v)

   print(dict_1.keys())  
   print(dict_1.values())

   dict_2 = dict_1.copy()

   dict_3 = dict_1

   dict_3["ravi"] = 50

   print(dict_3)
   print(dict_1)