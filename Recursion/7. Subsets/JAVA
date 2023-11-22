// https://leetcode.com/problems/subsets

class Solution {

    public void helper(int[] nums, int ind, List<Integer> curr, List<List<Integer>> res) {
        if(ind == nums.length) {
            res.add(new ArrayList<> (curr));
            return;
        }

        //inc
        curr.add(nums[ind]);
        helper(nums, ind+1, curr, res);
        curr.remove(curr.size() - 1);

        //exc
        helper(nums, ind+1, curr, res);
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> curr = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        helper(nums, 0, curr, res);
        return res;
    }
}