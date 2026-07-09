class Solution:
    def minimumSteps(self, s: str) -> int:
        total_swaps = 0
        insert_pos = 0 
        for current, int in enumerate(s):
            if int == '0':
                total_swaps += (current - insert_pos)
                
                insert_pos += 1
                
        return total_swaps
