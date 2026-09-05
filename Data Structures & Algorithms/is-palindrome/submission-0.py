class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first instinct i have is to get rid of the spaces and make it an array of character then just do two pointer 

        s = ''.join(c.lower() for c in s if c.isalnum())


        
        #dont think i need the spaces removed

        left = 0
        right = len(s)-1


        while(left < right):

            if (s[left]!=s[right]):
                
                return False
            left+=1
            right -=1

        return True
        