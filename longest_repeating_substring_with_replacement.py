class Solution():
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = dict()
        most_nums = 0
        longest_seq = 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            most_nums = max(most_nums, count[s[i]])
            if (i-l+1) - most_nums > k:
                count[s[l]]-= 1
                l+=1
            print(l, i)
            longest_seq = max(longest_seq, i - l + 1)
        return longest_seq
Test = Solution()
print(Test.characterReplacement("AABB", 2))


