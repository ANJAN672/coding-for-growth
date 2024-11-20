class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        hashmap={")":"(","]":"[","}":"{"}
        for i in s:
            if i not in hashmap:
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    popped=stk.pop()
                    if popped !=hashmap[i]:
                        return False
        return not stk  