class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=0
        #nspace efficient yet not time

        while i < len(intervals)-1:
            if intervals[i+1][0] <= intervals[i][1]:
                # merge
                intervals[i] = [
                    intervals[i][0],
                    max(intervals[i][1], intervals[i+1][1])]
                intervals.pop(i+1)  # safer than remove
                # DON'T increment i → check again with new next interval
            else:
                i += 1
        
        return intervals




        