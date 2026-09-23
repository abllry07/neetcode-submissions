class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count = 0

        for w in words:
            plus = 1
            for c in w:
                if c not in allowed:
                    plus = 0
                    break
            count += plus
    
        return count