# recursive n to 0
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        return self.decode(len(s)-1,s)

    def decode(self,index,s)->int:
        if index<=0:
            return 1
        result=0
        if s[index]!='0':
            result=self.decode(index-1,s)
        if (s[index-1]=='1'or (s[index-1]=='2' and s[index]<'7' and s[index]>='0')):
            result+=self.decode(index-2,s)
        return result

# REcursive 0 to n
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        return self.decode(0,s,len(s))
    def decode(self,index,s,n)->int:
        if index==n:
            return 1
        if s[index]=='0':
            return 0        
        result=self.decode(index+1,s,n)
        if index<n-1 and (s[index]=='1' or (s[index]=='2' and s[index+1]<'7')):
            result+=self.decode(index+2,s,n)
        return result

# Top down DP(memoization)
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        n=len(s)
        dp=[-1]*(n+1)
        dp[n]=1
        return self.decode(n-1,s,dp)
    def decode(self,index,s,dp)->int:
        if index<=0:
            return 1
        if dp[index] !=-1:
            # print(dp)
            return dp[index]
        result=0
        if s[index]!='0':
            result=self.decode(index-1,s,dp)
        if s[index-1]=='1' or (s[index-1]=='2' and s[index]>='0' and s[index]<'7'):            
                result+=self.decode(index-2,s,dp)            
        # print(dp)
        dp[index]=result
        return dp[index]
        
# Bottom up DP
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1

        for index in range(1,n+1):
            if s[index-1]!='0':
                dp[index]+=dp[index-1]
            if index>1 and s[index-2:index]>='10' and s[index-2:index]<='26':
                dp[index]+=dp[index-2]
        print(dp)
        return dp[n]

# Space Optimization
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        forward_once,forward_twice=1,0
        n=len(s)
        for index in range(1,n+1):
            ans=0
            if s[index-1]!='0':
                ans+=forward_once
            if index>1 and s[index-2:index]>='10' and s[index-2:index]<='26':
                ans+=forward_twice
            forward_twice=forward_once
            forward_once=ans
        return forward_once