class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(num: str, index: int, target: int) -> bool:
            if index == len(num):
                return target == 0

            sum_val = 0
            for i in range(index, len(num)):
                sum_val = sum_val * 10 + int(num[i])
                if sum_val > target:
                    break
                if canPartition(num, i + 1, target - sum_val):
                    return True
            return False

        total=0
        for i in range(1,n+1):
            sq=i*i
            if canPartition(str(sq),0,i):
                total+=sq
        return total