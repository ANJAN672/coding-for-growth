class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashm = {} 
        maxm = -1   
        
        for num in nums:
            sumi = sum(map(int, str(num)))  
            
            if sumi in hashm:
                maxm = max(maxm, num + hashm[sumi][0])
                hashm[sumi] = [max(num, hashm[sumi][0]), min(num, hashm[sumi][0])]
            else:
                hashm[sumi] = [num] 
                
        return maxm