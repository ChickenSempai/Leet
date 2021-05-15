class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        crs.assign(numCourses, list <int>());
        visited.assign(numCourses, false);
        dfsPath.assign(numCourses, false);
        for(auto req: prerequisites){
            crs[req[1]].push_back(req[0]);
        }
        for (int i=0; i < numCourses; i++){
            if (dfs(i))
                return false; 
        }
        return true;
    }
private:
    vector <bool> visited;
    vector <list<int>> crs;
    bool dfs(int node){
        dfsPath[node] = true;
        visited[node] = true;
        for (auto next: crs[node]){
            if (dfsPath[next])
                return true;
            if (!visited[next])
                if(dfs(next))
                    return true;
        }
        dfsPath[node] = false;
        return false;
    }
    vector <bool> dfsPath;
};