// https://leetcode.com/problems/decode-ways

//Solution 1 - n to 0

class Solution {
public:
    int helper(string s, int ind, int n) {
        if(ind <= 0) return 1;
        int res = 0;
        if(s[ind] != '0') res = helper(s, ind-1, n);

        if((s[ind-1] == '1') || (s[ind-1] == '2' && s[ind] >= '0' && s[ind] <= '6'))
        {
            res += helper(s, ind-2, n);
        }
        return res;
    }

    int numDecodings(string s) {
        int n = s.length();
        if(s[0] == '0') return 0;
        return helper(s, n-1, n);
    }
};

//Solution 2 - 0 to n

class Solution {
public:
    int helper(string& s, int index, int len){
        if(index == len)return  1;

        if(s[index] == '0')return 0;

        int res = helper(s, index + 1, len);
        if(index < len - 1 &&
         (s[index] == '1' || (s[index] == '2' && s[index + 1] < '7'))){
            res += helper(s, index + 2, len);
        }
        return res;
    }

    int numDecodings(string s) {
        return helper(s, 0, s.size());
    }
};
