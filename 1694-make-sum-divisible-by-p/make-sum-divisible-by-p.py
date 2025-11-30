class Solution(object):
    def minSubarray(self, nums, p):
        """
        Find minimum length subarray to remove so remaining sum is divisible by p
        
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        s = sum(nums)           # total sum of array
        t = s % p               # target remainder to remove
        
        # 🎯 BASE CASE: Already divisible
        if t == 0:
            return 0
        
        h = {0: -1}             # maps {remainder : last_index}
        pre_sum = 0             # running prefix sum
        min_len = len(nums)     # track minimum subarray length
        
        for i in range(len(nums)):
            pre_sum += nums[i]
            rem = pre_sum % p   # current prefix remainder
            
            # 🔍 KEY FORMULA: Find needed previous remainder
            n = (rem - t + p) % p
            
            # ✨ CHECK: If needed remainder exists in hashmap
            if n in h:
                min_len = min(min_len, i - h[n])
            
            # 💾 STORE: Current remainder with its index
            h[rem] = i
        
        # 🚀 RETURN: Min length if valid, else -1
        return min_len if min_len < len(nums) else -1