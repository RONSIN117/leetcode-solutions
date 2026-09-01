class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        from collections import deque
        
        rows = len(classroom)
        cols = len(classroom[0])
        
        start_r = start_c = -1
        litters = {}
        litter_idx = 0
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litters[(r, c)] = litter_idx
                    litter_idx += 1
                    
        target_mask = (1 << litter_idx) - 1
        if target_mask == 0:
            return 0
        queue = deque([(0, start_r, start_c, energy, 0)])
        visited = {(start_r, start_c, 0): energy}
        
        while queue:
            moves, r, c, cur_energy, mask = queue.popleft()
            
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                

                if 0 <= nr < rows and 0 <= nc < cols and classroom[nr][nc] != 'X':
                    nxt_energy = cur_energy - 1
                    
                    if nxt_energy < 0:
                        continue
                        
                    nxt_mask = mask
                    if classroom[nr][nc] == 'L':
                        nxt_mask |= (1 << litters[(nr, nc)])
                        
                    if nxt_mask == target_mask:
                        return moves + 1
                        
                    if classroom[nr][nc] == 'R':
                        nxt_energy = energy
                    if nxt_energy > visited.get((nr, nc, nxt_mask), -1):
                        visited[(nr, nc, nxt_mask)] = nxt_energy
                        queue.append((moves + 1, nr, nc, nxt_energy, nxt_mask))
                        
        return -1