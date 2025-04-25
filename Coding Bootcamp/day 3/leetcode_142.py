# 142. Linked List Cycle II

class Solution(object):
    def detectCycle(self, head):
        Fast = head 
        Slow = head
        
        while(Fast is not None and Fast.next is not None):
            Fast = Fast.next.next
            Slow = Slow.next
            if(Fast == Slow):
                Slow = head
                while(Fast != Slow):
                    Slow = Slow.next
                    Fast = Fast.next
                return Slow
        return None
