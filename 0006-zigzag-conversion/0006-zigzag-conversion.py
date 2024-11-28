class Solution:
    def convert(self, s: str, numRows: int) -> str:
        my_list = [""]*numRows
        ind = 0
        flag = True
        if numRows == 1:
            return s
        for i in s:
            my_list[ind] += i
            if ind == numRows-1:
                flag = False
            if ind == 0:
                flag = True
            if flag == True:
                ind += 1
            if flag == False:
                ind -= 1
        return "".join(my_list)