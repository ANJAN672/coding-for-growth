class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        for o in operations:
            if o=="C":
                stk.pop()
            elif o=="D":
                stk.append(stk[-1]*2)
            elif o=="+":
                stk.append(stk[-1]+stk[-2])
            else:
                stk.append(int(o))
        return sum(stk)
        