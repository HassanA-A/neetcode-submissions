class Solution:

    def encode(self, strs: List[str]) -> str:

        #Understand: TAke an array of strings and output it all in one string with some kind of delimeter to seperate each string for when u decode

        stringy=""
        for i in strs:
            stringy += str(len(i))+'%'+i
        return stringy

    def decode(self, s: str) -> List[str]:

        x = 0
        strs = []
        while x < len(s):
            #Take the number skip the next character and then add that substring based onlength to the array
            # Find the %
            percent = s.index('%', x)

            # Get the length
            length = int(s[x:percent])

            # Start after %
            start = percent + 1

            # Take 'length' characters
            word = s[start:start + length]

            strs.append(word)

            # Move x to the next encoded string
            x = start + length


        return strs
