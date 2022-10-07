class Solution:
    def isValid(self, s: str) -> bool:
        
        lookup_table = {'(':')','{':'}','[':']'}
        seen = []
        
        for i in s:
            
            if i in lookup_table:
                seen.append(i)
                #[()()]
            elif not seen or i != lookup_table[seen.pop()]:
                False
                
            # elif not seen:
            #     return False
            
        return not seen