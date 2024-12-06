class LinkedList()
  def __init(self, data):
          self.data = data
          self.next = None
        
  def reverseList(self):
        prev, curr = None, self.head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

if __name__ == '__main__':
  # lst = [1,2,3,4]
  ll = LinkedList()   
  ll.append(1)
  ll.append(2)
        
  print(ll)
  ll.reverseList()
  print(ll)      
