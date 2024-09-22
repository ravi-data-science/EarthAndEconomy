from collections import deque

if __name__ == '__main__':

   set1 = {32, 1, 2, 27, 83, 26, 59, 60}
   set1_odd = [i for i in set1 if i % 2 == 1]
   print(set1_odd)

   for i in set1:
      print(i)