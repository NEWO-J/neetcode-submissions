use std::collections::HashMap;
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut seenmap = HashMap::new();
        let mut seenmap2 = HashMap::new();
        for i in s.chars() {
            *seenmap.entry(i).or_insert(0) += 1;
        }
        for i in t.chars() {
            *seenmap2.entry(i).or_insert(0) += 1;
        }
        if seenmap == seenmap2 {
                return true;
            }
            else {
                return false;
            }
    }
}
