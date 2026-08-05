class Solution(object):
    def remainingMethods(self, n, k, invocations):
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        suspicious = set([k])
        queue = [k]
        
        for node in queue:
            for neighbor in adj[node]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        can_remove = True
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                can_remove = False
                break
                
        if not can_remove:
            return list(range(n))
            
        return [i for i in range(n) if i not in suspicious]