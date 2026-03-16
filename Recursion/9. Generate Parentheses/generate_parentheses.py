# https://leetcode.com/problems/generate-parentheses

# Actual problem: make n well-formed pair of parentheses
# Sub-problem: make 1,2,.....n-1,n pair of well-formed parentheses
# Bottom-up approach
# visualization: https://www.recursionvisualizer.com/?function_definition=def%20generator%28n%2CnumClosed%2CnumOpen%2CcurrString%2Cresult%29%3A%0A%20%20%20%20%20%20%20%20if%20numClosed%3D%3Dn%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result.append%28currString%29%0A%20%20%20%20%20%20%20%20%20%20%20%20return%0A%20%20%20%20%20%20%20%20%23%20include%20close%0A%20%20%20%20%20%20%20%20if%20numOpen%3EnumClosed%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20generator%28n%2CnumClosed%2B1%2CnumOpen%2CcurrString%2B'%29'%2Cresult%29%0A%20%20%20%20%20%20%20%20%23%20include%20open%0A%20%20%20%20%20%20%20%20if%20numOpen%3Cn%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20generator%28n%2CnumClosed%2CnumOpen%2B1%2CcurrString%2B'%28'%2Cresult%29&function_call=generator%283%2C0%2C0%2C%22%22%2C%5B%5D%29

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result,currString=[],""
        self.generator(n,0,0,currString,result)
        return result
    def generator(self,n,numClosed,numOpen,currString,result):
        if numClosed==n:
            result.append(currString)
            return
        # include close
        if numOpen>numClosed:
            self.generator(n,numClosed+1,numOpen,currString+')',result)
        # include open
        if numOpen<n:
            self.generator(n,numClosed,numOpen+1,currString+'(',result)