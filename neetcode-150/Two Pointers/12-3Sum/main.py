class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum = nums[j] + nums[k]
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    j += 1
                    k -= 1
                    
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return result
