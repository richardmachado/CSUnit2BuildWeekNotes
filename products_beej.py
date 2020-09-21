"""
We have an array of at least 2 ints

We have n inputs in the array
We have n outputs in the output array

Each output is the product of all the inputs, except the input at the index of the output.

Simplify the problem:

Each output is the product of all the inputs at indexes _less than_ the current index.
Each output is the product of all the inputs at indexes _greater than_ the current index.

[1, 2, 3, 4, 5]
[1, 2, 6, 24,120]

[1, 2, 3, 4, 5]
[120, 120, 60, 20, 5]


Put simplified problems together:

   >   <
[1,2,3,4,5]
1 2 6 24 120        Forward products
120  120  60  20 5  Backward products

[1,2,3,4]  product = 24
[24, 24, 24, 24]
[24, 12, 8, 6]

[1,2]
[2,1]


[0,1,2,3]  product = 0
[6,0,0,0]

https://leetcode.com/problems/product-of-array-except-self/submissions/
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            output.append(product)
            
        return output


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        nonzero_product = 1
        
        zero_count = 0
        zero_index = None
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                zero_index = i
            else:
                nonzero_product *= nums[i]
                
            product *= nums[i]
            
        if zero_count > 1:
            return [0] * len(nums)
        
        if zero_count == 1:
            output = [0] * len(nums)
            output[zero_index] = nonzero_product
            
            return output
            
        output = [product] * len(nums)

        for i in range(len(output)):
            output[i] //= nums[i]
            
        return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        
        forward_products = [1] * len(nums)
        backward_products = [1] * len(nums)
        
        for i in range(len(nums)):
            p *= nums[i]
            forward_products[i] = p
            
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            p *= nums[i]
            backward_products[i] = p
            
        output = []
        
        for i in range(len(nums)):
            if i == 0:
                output.append(backward_products[i+1])
                
            elif i == len(nums) - 1:
                output.append(forward_products[i-1])
                
            else:
                p = forward_products[i-1] * backward_products[i+1]
                output.append(p)

        return output
