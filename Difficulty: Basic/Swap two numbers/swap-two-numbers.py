class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        a = a^b
        b = a^b
        a = b^a
    
        return a,b