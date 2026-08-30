class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Understand: an array of strings that u gotta group up if they share the same character
        #Plan: Iterate through and compare each string to one another
        #Execution

        groups = {}
        for i in strs:
            
            key = ''.join(sorted(i))
            if key not in groups:
                groups[key] = []
            groups[key].append(i)
        return list(groups.values())