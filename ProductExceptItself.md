class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        forward_products = [1] * len(nums)
        backward_products = [1] * len(nums)
        
        for i in range(len(nums)):
            p *= nums[i]
            forward_products[i] = p 
            
        p = 1
        for i in range(len(nums) -1, -1, -1):
            p *=nums[i]
            backward_products[i] = p
            
        output = []
        
        for i in range(len(nums)):
            if i == 0:
                output.append(backward_products[i+1])
            elif i == len(nums)-1:
                output.append(forward_products[i-1])
            else:
                p = forward_products[i-1] * backward_products[i+1]
                output.append(p)
                
        return output