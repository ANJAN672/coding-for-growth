class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        ind=[]
        if len(s)!=len(goal):
            return False
        if s == goal:
            return True if abs(len(set(s)) - len(goal)) >= 1 else False

        for i in range(len(goal)):
            if s[i]!=goal[i]:
                ind.append(i)

        if len(ind)>2 or len(ind)!=2:
            return False
        print(ind)
        if s[ind[0]]==goal[ind[1]] and s[ind[1]]==goal[ind[0]]:
            return True
        return False