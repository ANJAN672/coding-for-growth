class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ind=[]
        if s1==s2:
            return True

        for i in range(0,len(s2)):
            if s1[i]!=s2[i]:
                ind.append(i)
        # print(ind)
        if len(ind)>2 or len(ind) != 2:
            return False
        else:
            i,j=ind
            s2_list=list(s2)
            s2_list[i],s2_list[j]=s2_list[j],s2_list[i]
            return "".join(s2_list)==s1
        return False
