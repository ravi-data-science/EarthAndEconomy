def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

if __name__ == '__main__':
  lst = [1,2,3,4]
  print(reverseList(lst))
