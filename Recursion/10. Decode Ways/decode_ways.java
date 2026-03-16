// https://leetcode.com/problems/decode-ways

class Solution {

    public int helper(String s, int ind, int n) {
        if(ind <= 0) return 1;
        int res = 0;
        if(s.charAt(ind) != '0') res += helper(s, ind-1, n);
        if((s.charAt(ind-1) == '1') || (s.charAt(ind-1) == '2' && s.charAt(ind) >= '0' && s.charAt(ind) <= '6')) {
            res += helper(s, ind-2, n);
        }
        return res;
    }
    
    public int numDecodings(String s) {
        if(s.charAt(0) == '0') return 0;
        int n = s.length();
        return helper(s, n-1, n);
    }
}

