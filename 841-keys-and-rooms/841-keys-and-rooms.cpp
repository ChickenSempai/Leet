class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        std::bitset<1000> visited;
        std::queue<int> q;
        q.push(0);
        while(!q.empty()){
            auto curr = q.front();
            if (!visited[curr]){
                visited.set(curr);
                for(auto& key: rooms[curr])
                    q.push(key);
            }
            q.pop();
        }
        return visited.count() == rooms.size();
    }
};