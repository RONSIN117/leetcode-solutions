class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
            
        prev = head
        curr = head.next
        idx = 1
        
        first_crit = -1
        last_crit = -1
        min_dist = float('inf')
        
        while curr.next:
            nxt = curr.next
            
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):
                
                if first_crit == -1:
                    first_crit = idx
                else:
                    min_dist = min(min_dist, idx - last_crit)
                    
                last_crit = idx
                
            prev = curr
            curr = nxt
            idx += 1
            
        if min_dist == float('inf'):
            return [-1, -1]
            
        return [min_dist, last_crit - first_crit]