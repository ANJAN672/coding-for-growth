class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        # Compute LCS table
        lcs = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    lcs[i][j] = 1 + lcs[i - 1][j - 1]
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

        # Build the shortest supersequence
        i, j = m, n
        result = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i, j = i - 1, j - 1
            elif lcs[i - 1][j] > lcs[i][j - 1]:
                result.append(str1[i - 1])
                i -= 1
            else:
                result.append(str2[j - 1])
                j -= 1

        while i > 0:
            result.append(str1[i-1])
            i -= 1
        
        while j > 0:
            result.append(str2[j-1])
            j -= 1

        return "".join(result[::-1])