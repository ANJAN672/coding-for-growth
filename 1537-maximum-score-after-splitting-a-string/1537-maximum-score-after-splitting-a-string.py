class Solution:
    def maxScore(self, s: str) -> int:
        max_count=0
        count_left_zeros=0
        count_right_ones=s.count('1')

        for i in range(len(s)-1):
            count_left_zeros+=s[i]=='0'
            count_right_ones-=s[i]=='1'
            max_count=max(max_count,count_left_zeros+count_right_ones)
        return max_count