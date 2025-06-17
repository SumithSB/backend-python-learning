class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result = []

        if len(word1) == len(word2):
            for l1,l2 in word1,word2:
                result.append(l1,l2)
        



ans  = Solution()

print(ans.mergeAlternately("abc","pqr"))