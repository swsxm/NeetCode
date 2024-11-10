class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_dict = dict()
        have_dict = dict()
        need = len(t)
        have = 0
        min = ""
        l = 0
        
        for c in t:
            need_dict[c] = need_dict.get(c, 0) + 1
            have_dict[c] = 0

        for i in range(len(s)):

            # check if need == have then we can slide the l pointer to the r
            if s[i] in have_dict: 
                have_dict[s[i]] += 1
                if have_dict[s[i]] <= need_dict[s[i]]:
                    have += 1
            while need == have:
                min = s[l:i+1] if (i-l < len(min) or min == "") else min
                if s[l] in have_dict:
                    have_dict[s[l]] -= 1
                    if need_dict[s[l]] > have_dict[s[l]]:
                        have -= 1
                l += 1

        return min



                

Test = Solution()
s = "aa"
t = "a"
print(": ", Test.minWindow(s, t))

