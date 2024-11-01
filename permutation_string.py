class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            print('wtf')
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26

        for char in s1:
            s1_count[ord(char) - ord('a')] += 1 
        l = 0
        for i in range(len(s2)):
            s2_count[ord(s2[i]) - ord('a')] += 1
            if i - l + 1 > len(s1):
                s2_count[ord(s2[l]) - ord('a')] -= 1
                l+=1
            print(l, i)
            if s1_count == s2_count:
                return True
        
        return False


Test = Solution()
print(Test.checkInclusion("ky", "ainwkckifykxlribaypk"))
