class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;
        vector<vector<string>> result;
        for(int i=0;i<strs.size();i++){
            string ss;
            ss=strs[i];
            sort(ss.begin(),ss.end());
            hashmap[ss].push_back(strs[i]);
        }
        for(auto& entry:hashmap){
            result.push_back(entry.second);
        }
        return result;
    }
};
