class Solution:
    def maxSubarraySum(self, a: List[int], k: int) -> int:
        res,p = -inf,[0,*accumulate(a)]
        for i in range(k):
            q = -inf
            for j in range(i+k,len(p),k):
                v = p[j]-p[j-k]
                q = max(v,q+v)
                res = max(res,q)
                
        return res