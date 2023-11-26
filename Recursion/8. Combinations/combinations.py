# https//leetcode.com/problems/combinations

# Actaul problem: make combinations of n numbers.
# Sub problem: make combinations of n-1(top down) numbers or 1,2....n-1,n numbers(bottom-up).

# Bottom-up approach

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        currentCombination,result=[],[]
        self.makeCombinations(k,n,1,currentCombination,result)
        return result
    def makeCombinations(self,k:int,n:int,index:int,currentCombination: List[int],result: List[List[int]]):
        if len(currentCombination)==k:
            result.append(currentCombination.copy())
            return
        if index>n:
            return
        # include
        currentCombination.append(index)
        self.makeCombinations(k,n,index+1,currentCombination,result)
        # exclude
        currentCombination.pop()
        self.makeCombinations(k,n,index+1,currentCombination,result)

# Top down approach

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        currentCombination,result=[],[]
        self.makeCombinations(k,n,n,currentCombination,result)
        return result
    def makeCombinations(self,k:int,n:int,index:int,currentCombination: List[int],result: List[List[int]]):
        if len(currentCombination)==k:
            result.append(currentCombination.copy())
            return
        if index<1:
            return
        # include
        currentCombination.append(index)
        self.makeCombinations(k,n,index-1,currentCombination,result)
        # exclude
        currentCombination.pop()
        self.makeCombinations(k,n,index-1,currentCombination,result)