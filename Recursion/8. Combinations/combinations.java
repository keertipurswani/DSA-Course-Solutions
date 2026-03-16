//https://leetcode.com/problems/combinations

class Solution {

    public void helper(int n, int k, int i, List<Integer> curr, List<List<Integer>> res) {
        if(curr.size() == k) {
            res.add(new ArrayList<> (curr));
            return;
        }
        if(i > n) return;

        //inc
        curr.add(i);
        helper(n, k, i+1, curr, res);
        curr.remove(curr.size() - 1);

        //exc
        helper(n, k, i+1, curr, res);
    }

    public List<List<Integer>> combine(int n, int k) {
        List<Integer> curr = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        helper(n, k, 1, curr, res);
        return res;
    }
}