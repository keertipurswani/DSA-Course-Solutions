// https://leetcode.com/problems/generate-parentheses

class Solution {
    public void helper(int o, int c, int n, String curr, List<String> res) {
        if(c == n) {
            res.add(curr);
            return;
        }
        if(o>c) helper(o, c+1, n, curr + ')', res);
        if(o<n) helper(o+1, c, n, curr + '(', res);
    }

    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        helper(0, 0, n, "", res);
        return res;
    }
}