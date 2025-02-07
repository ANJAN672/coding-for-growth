from collections import Counter
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color=Counter()
        color_count=Counter()
        res=[]

        for x,y in queries:
            old_color=ball_color.get(x,None)
            if old_color in color_count:
                color_count[old_color]-=1
            if color_count[old_color]==0:
                del color_count[old_color]
            ball_color[x]=y
            color_count[y]+=1
            # print("ball_color:",ball_color)
            # print("color_count:",color_count)
            res.append(len(color_count))
        return res