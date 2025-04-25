class Solution(object):
    def hasCycle(self, head):
      fast = head
      slow = head
      while(fast.next.next):
        if(fast==slow):
            return True
        slow = slow.next
        fast = fast.next.next
        return False