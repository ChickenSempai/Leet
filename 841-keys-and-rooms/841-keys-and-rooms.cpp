class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        std::unordered_set<int> visited;
        std::queue<int> q;
        q.push(0);
        while(!q.empty()){
            auto curr = q.front();
            if (visited.find(curr) == visited.end()){
                visited.insert(curr);
                for(auto& key: rooms[curr])
                    q.push(key);
            }
            q.pop();
        }
        if (visited.size() == rooms.size())
            return true;
        return false;
    }
};