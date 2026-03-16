# https://leetcode.com/problems/subsets


# Actual problem: find subsets of n elements in an array
# Sub-Problem: find subsets of n-1, n-2....0 elements or 0,1.....(n-1),n elements
# Bottom-up approach(0 to n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result,currentSubset=[],[]
        self.makeSubsets(nums,0,currentSubset,result)
        return result
    def makeSubsets(self,nums: List[int],index: int,currentSubset: List[int],result: List[List[int]]):
        if index==len(nums):
            result.append(currentSubset.copy())            
            return
        # include
        currentSubset.append(nums[index])
        self.makeSubsets(nums,index+1,currentSubset,result)
        # exclude
        currentSubset.pop()
        self.makeSubsets(nums,index+1,currentSubset,result)

# Top-down approach(n to 0)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result,currentSubset=[],[]
        self.makeSubsets(nums,len(nums)-1,currentSubset,result)
        return result
    def makeSubsets(self,nums: List[int],index:int,currentSubset: List[int],result: List[List[int]]):
        if index<0:
            result.append(currentSubset.copy())
            return
        # include
        currentSubset.append(nums[index])
        self.makeSubsets(nums,index-1,currentSubset,result)
        # exclude
        currentSubset.pop()
        self.makeSubsets(nums,index-1,currentSubset,result)