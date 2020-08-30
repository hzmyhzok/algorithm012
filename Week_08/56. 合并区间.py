class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        res = []
        intervals.sort(key=lambda x: x[0])  
        for inter in intervals:
            if len(res) == 0 or res[-1][1] < inter[0]:  
                res.append(inter)
            else:  
                res[-1][1] = max(res[-1][1], inter[1])
        return res