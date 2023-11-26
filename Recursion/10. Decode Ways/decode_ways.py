# https://leetcode.com/problems/decode-ways/description/

# Actual problem: Decode string of n characters
# Sub-problem: Decode string of n-1,n-2,.....1,0 characters
# Top-down approach(n to 0)
# Visualization: https://www.recursionvisualizer.com/?function_definition=def%20decodeString%28index%2CinputString%29-%3Eint%3A%0A%20%20%20%20%20%20%20%20if%20index%3C%3D0%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20%20%20%20%20result%3D0%0A%20%20%20%20%20%20%20%20if%20inputString%5Bindex%5D!%3D'0'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result%3DdecodeString%28index-1%2CinputString%29%0A%20%20%20%20%20%20%20%20if%20%28inputString%5Bindex-1%5D%3D%3D'1'%20or%20%28inputString%5Bindex-1%5D%3D%3D'2'%20and%20inputString%5Bindex%5D%3E%3D'0'%20and%20inputString%5Bindex%5D%3C%3D'6'%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result%2B%3DdecodeString%28index-2%2CinputString%29%0A%20%20%20%20%20%20%20%20return%20result&function_call=decodeString%283%2C%221111%22%29


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        return self.decodeString(len(s)-1,s)
    def decodeString(self,index:int,inputString: str)->int:
        if index<=0:
            return 1
        result=0
        if inputString[index]!='0':
            result=self.decodeString(index-1,inputString)
        if (inputString[index-1]=='1' or (inputString[index-1]=='2' and inputString[index]>='0' and inputString[index-1]<='6')):
            result+=self.decodeString(index-2,inputString)
        return result

# Bottom-up approach(0 to n)

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        return self.decodeString(s,0,len(s))
    def decodeString(self,inputString: str, index: int,n: int)->int:
        if index==n:
            return 1
        if inputString[index]=='0':
            return 0
        result=self.decodeString(inputString,index+1,n)
        if index<n-1 and (inputString[index]=='1'or (inputString[index]=='2' and inputString[index+1]<'7')):
            result+=self.decodeString(inputString,index+2,n)
        return result