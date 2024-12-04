class Solution:
    def isHappy(self, n: int) -> bool:
        lookup = set()
        luckynumber = 0
        while luckynumber != 1 and luckynumber not in lookup:
            luckynumber = 0
            for num in str(n):
                luckynumber += int(num) ** 2
            lookup.add(luckynumber)
            n = luckynumber
        return luckynumber == 1
