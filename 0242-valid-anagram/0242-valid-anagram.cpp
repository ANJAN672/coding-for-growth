class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length()!=t.length()){
            return false;
        }
        unordered_map<char,int> hashmap;

        for(int i=0;i<s.length();i++){
            hashmap[s[i]]++;
        }
        for(int i=0;i<t.length();i++){
            hashmap[t[i]]--;
        }
        for(auto& entry:hashmap){
            if(entry.second!=0){
                return false;
            }
        }
        return true;
    }
};