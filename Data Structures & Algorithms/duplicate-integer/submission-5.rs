use std::collections::HashMap;
impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut hmap = HashMap::new();
        for i in nums {
            if hmap.contains_key(&i) {
                return true;
            } else {
                hmap.insert(i, 1);
            }
        }
        return false;
    }
}
