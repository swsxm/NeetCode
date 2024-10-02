class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = dict()
        
        for s_char, t_char in zip(s, t):
            hashmap[s_char] = hashmap.get(s_char, 0) + 1
            hashmap[t_char] = hashmap.get(t_char, 0) - 1

        for key in hashmap:
            if hashmap[key] != 0:
                return False
        return True

Test = Solution()
print(Test.isAnagram(s = "jar", t = "jam"))
