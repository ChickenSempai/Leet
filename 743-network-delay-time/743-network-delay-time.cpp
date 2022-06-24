class Solution {
public:
    
    class Node {
    public:
        Node(int val){
            this->val = val;
        };
        int val;
        std::vector<int> neibs;
        std::vector<int> lens;
    };
    
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        std::vector<Node> nodes(n, Node(-1));
        for(auto& time: times){
            nodes[time[0]-1].neibs.push_back(time[1]);
            nodes[time[0]-1].lens.push_back(time[2]);
        }
        std::priority_queue<pair<int, int>> q;
        q.push(make_pair(0, k));
        while(!q.empty()){
            auto curr = q.top();
            q.pop();
            if (nodes[curr.second-1].val == -1){
                nodes[curr.second-1].val = -curr.first;
                for(size_t i = 0; i < nodes[curr.second-1].neibs.size(); i++){
                    q.push(make_pair(-(nodes[curr.second-1].lens[i] + nodes[curr.second-1].val), nodes[curr.second-1].neibs[i]));
                }
            }
        }
        int maxx = 0;
        for(auto& node: nodes){
            if (node.val == -1)
                return -1;
            maxx = std::max(node.val, maxx);
        }
        return maxx;
    }
};