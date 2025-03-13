class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr.sort()
        
        min_diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] < min_diff:
                min_diff = arr[i] - arr[i - 1]
        
        i = 0
        while i < len(arr) - 1:
            if arr[i + 1] - arr[i] == min_diff:
                res.append([arr[i], arr[i + 1]])
            
            i += 1
                
        
    
        return res
