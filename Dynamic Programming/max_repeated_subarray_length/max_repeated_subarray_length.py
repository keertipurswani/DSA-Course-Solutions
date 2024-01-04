# recursive 0 to n.
# TC: O(2^(n+m)), SC: O(n+m), where n and m are length of nums1 and nums2 respectively
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:        
        return self.findMaxSubarray(nums1,nums2,0,0,0)
    def findMaxSubarray(self,nums1,nums2,ind1,ind2,max_subarray_length):
        if ind1>=len(nums1) or ind2>=len(nums2):            
            return max_subarray_length        
        if nums1[ind1]==nums2[ind2]:
            max_subarray_length=self.findMaxSubarray(nums1,nums2,ind1+1, ind2+1,max_subarray_length+1)        
        max_subarray_length= max(max_subarray_length,self.findMaxSubarray(nums1,nums2,ind1,ind2+1,0),self.findMaxSubarray(nums1,nums2,ind1+1,ind2,0))                
        return max_subarray_length


# Top Down DP(memoization)
# TC: O(2^(n+m)), SC: O(n*m)+O(n+m), where n and m are length of nums1 and nums2 respectively
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n,m=len(nums1),len(nums2)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        self.findMaxSubarray(nums1,nums2,n,m,dp)
        return max(chain(*dp))
    def findMaxSubarray(self,nums1,nums2,ind1,ind2,dp):
        if ind1==0 or ind2==0:
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]            
        if nums1[ind1-1]==nums2[ind2-1]:
            dp[ind1][ind2]=1+self.findMaxSubarray(nums1,nums2,ind1-1, ind2-1,dp)
        else:
            dp[ind1][ind2]=0
        self.findMaxSubarray(nums1,nums2,ind1-1,ind2,dp)
        self.findMaxSubarray(nums1,nums2,ind1,ind2-1,dp)
        return dp[ind1][ind2]

# Bottom Up DP(tabulation)
# TC: O(n*m), SC: O(n*m), where n and m are length of nums1 and nums2 respectively
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n,m=len(nums1),len(nums2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        max_subarray_length=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    max_subarray_length=max(max_subarray_length,dp[i][j])
                else:
                    dp[i][j]=0
        return max_subarray_length

# Space optimization
# TC: O(n*m), SC: O(1), where n and m are length of nums1 and nums2 respectively
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n,m=len(nums1),len(nums2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        prev=[0]*(m+1)
        max_subarray_length=0
        for i in range(1,n+1):
            curr=[0]*(m+1)
            for j in range(1,m+1):
                if nums1[i-1]==nums2[j-1]:
                    curr[j]=1+prev[j-1]
                    max_subarray_length=max(max_subarray_length,curr[j])
                else:
                    curr[j]=0
            prev=curr
        return max_subarray_length
