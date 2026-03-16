# https://leetcode.com/problems/permutations

# Actual problem: find permutation of n given integer
# Sub problem: find permutation of n-1
# Top-down approach
# Visualization: https://www.recursionvisualizer.com/?function_definition=def%20findPermutations%28nums%2Cn%2Cindex%2Cresult%29%3A%0A%20%20%20%20%20%20%20%20if%20index%3D%3D0%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result.append%28nums.copy%28%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20return%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28index%2C-1%2C-1%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nums%5Bi%5D%2Cnums%5Bindex%5D%3Dnums%5Bindex%5D%2Cnums%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20findPermutations%28nums%2Cn%2Cindex-1%2Cresult%29%0A%20%20%20%20%20%20%20%20%20%20%20%20nums%5Bi%5D%2Cnums%5Bindex%5D%3Dnums%5Bindex%5D%2Cnums%5Bi%5D&function_call=findPermutations%28%5B1%2C2%2C3%5D%2C3%2C2%2C%5B%5D%29

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.findPermutations(nums,len(nums),len(nums)-1,result)
        return result
    def findPermutations(self,nums:List[int],n:int,index:int,result:List[List[int]]):
        if index==0:
            result.append(nums.copy())
            return
        for i in range(index,-1,-1):
            nums[i],nums[index]=nums[index],nums[i]
            self.findPermutations(nums,n,index-1,result)
            nums[i],nums[index]=nums[index],nums[i]

# Bottom-Up approach
# Visualization: https://www.recursionvisualizer.com/?function_definition=def%20findPermutations%28nums%2Cn%2Cindex%3Aint%2Cresult%3AList%5BList%5Bint%5D%5D%29%3A%0A%20%20%20%20%20%20%20%20if%20index%3D%3Dn%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result.append%28nums.copy%28%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20return%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28index%2Cn%2C1%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nums%5Bi%5D%2Cnums%5Bindex%5D%3Dnums%5Bindex%5D%2Cnums%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20findPermutations%28nums%2Cn%2Cindex%2B1%2Cresult%29%0A%20%20%20%20%20%20%20%20%20%20%20%20nums%5Bi%5D%2Cnums%5Bindex%5D%3Dnums%5Bindex%5D%2Cnums%5Bi%5D&function_call=findPermutations%28%5B1%2C2%2C3%5D%2C3%2C0%2C%5B%5D%29

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.findPermutations(nums,len(nums),0,result)
        return result
    def findPermutations(self,nums:List[int],n:int,index:int,result:List[List[int]]):
        if index==n:
            result.append(nums.copy())
            return
        for i in range(index,n,1):
            nums[i],nums[index]=nums[index],nums[i]
            self.findPermutations(nums,n,index+1,result)
            nums[i],nums[index]=nums[index],nums[i]