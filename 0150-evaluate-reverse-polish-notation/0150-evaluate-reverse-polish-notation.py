class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                stk.append(int(i))
            else:
                pop1=stk.pop()
                pop2=stk.pop()
                if i=="+":
                    stk.append(int(pop2)+int(pop1))
                elif i=="*":
                    stk.append(int(pop2)*int(pop1))
                elif i=="-":
                    stk.append(int(pop2)-int(pop1))
                elif i=="/":
                    stk.append(int(pop2/pop1))
        return stk[0]
                