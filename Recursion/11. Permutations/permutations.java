// https://leetcode.com/problems/permutations

//Solution 1 -> 0 to n

class Solution {
public:

    void helper(vector<vector<int>>& res, vector<int>& nums, int ind, int n) {
        if(ind == n) {res.push_back(nums); return;}
        
        for(int i = ind; i<n; i++) {
            swap(nums[i], nums[ind]);
            helper(res, nums, ind+1, n);
            swap(nums[i], nums[ind]);
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> curr;
        helper(res, nums, 0, nums.size());
        return res;
    }
};

//Solution 2 -> n-1 to 0

class Solution {

    private void helper(int ind, int[] nums, List<List<Integer>> ans) {
        if (ind == 0) {
            List <Integer> curr = new ArrayList <> ();
            for (int i = 0; i < nums.length; i++) {
                curr.add(nums[i]);
            }
            ans.add(new ArrayList <> (curr));
            return;
        }
        for (int i = ind; i >= 0; i--) {
            swap(i, ind, nums);
            helper(ind - 1, nums, ans);
            swap(i, ind, nums);
        }
    }
    private void swap(int i, int j, int[] nums) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList <> ();
        helper(nums.length - 1, nums, res);
        return res;
    }
}