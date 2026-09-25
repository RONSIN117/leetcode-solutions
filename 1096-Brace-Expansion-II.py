class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        union_sets = []
        current_concat_set = {""}
        
        for char in expression:
            if char.isalpha():
                current_concat_set = {s + char for s in current_concat_set}
            elif char == '{':
                stack.append((union_sets, current_concat_set))
                union_sets = []
                current_concat_set = {""}
            elif char == '}':
                union_sets.append(current_concat_set)
                block_set = set().union(*union_sets)
                
                prev_union_sets, prev_concat_set = stack.pop()
                current_concat_set = {p + t for p in prev_concat_set for t in block_set}
                union_sets = prev_union_sets
            elif char == ',':
                union_sets.append(current_concat_set)
                current_concat_set = {""}
                
        union_sets.append(current_concat_set)
        return sorted(list(set().union(*union_sets)))