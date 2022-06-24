class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        std::unordered_map<int, std::pair<int, int>> dict;
        if (n==1) return n;
        
        for(auto& p: trust){
            if (dict.find(p[0]) != dict.end())
                ++dict[p[0]].first;
            else
                dict[p[0]] = make_pair(1, 0);
            if (dict.find(p[1]) != dict.end())
                ++dict[p[1]].second;
            else
                dict[p[1]] = make_pair(0, 1);
            
        }
        for(auto i = dict.begin(); i != dict.end(); i++){
            if (i->second.first == 0 && i->second.second == dict.size()-1)
                return i->first;
        }
        return -1;
    }
};