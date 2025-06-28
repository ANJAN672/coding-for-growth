class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length()!=t.length()){
            return false;
        }
        unordered_map<char,int> hashmap;

        for(char c:s){
            hashmap[c]++;
        }
        for(char d:t){
            hashmap[d]--;
        }
        for(auto& entry:hashmap){
            if(entry.second!=0){
                return false;
            }
        }
        return true;
    }
};