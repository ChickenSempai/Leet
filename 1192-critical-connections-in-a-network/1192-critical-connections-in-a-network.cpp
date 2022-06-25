class Solution {
public:
    std::vector<std::vector<int>> res; 
    int dfs(std::vector<std::vector<int>>& nodes, int nid, std::vector<int>& steps, int step, int previd){
        if (steps[nid] == std::numeric_limits<int>::max()){
            steps[nid] = step;
            for(auto neib: nodes[nid]){
                if (neib != previd){
                    int retval = dfs(nodes, neib, steps, step+1, nid);
                    if (retval > step)
                        res.push_back({nid, neib});
                    steps[nid] = std::min(retval, steps[nid]);
                }   
            }
        }
        return steps[nid];
    }
    
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        std::vector<std::vector<int>> nodes(n);
        std::vector<int> steps(n, std::numeric_limits<int>::max());
        for(auto& con: connections){
            nodes[con[0]].push_back(con[1]);
            nodes[con[1]].push_back(con[0]);
        }
        dfs(nodes, 0, steps, 0, -1);
        return res;
    }
};