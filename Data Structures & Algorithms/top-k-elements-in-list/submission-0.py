class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Understand: we got a list of numbers and we gotta find the k most frequent numbers
        # Plan: Iterate throught the list once and then have a dictionary in that the key is the number the value is the number of it and then u just output the highest frequency values


        freq = {}

        for i in nums:

            if i not in freq:
                freq[i] = 1
            else:
                freq[i]= freq[i]+1
            
        
        sorted_by_value = sorted(freq.items(), key=lambda i: i[1], reverse=True)

        return [item[0] for item in sorted_by_value[:k]]