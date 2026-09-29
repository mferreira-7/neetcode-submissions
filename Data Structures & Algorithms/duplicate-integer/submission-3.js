class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate = (nums) => nums.length != new Set(nums).size

}
