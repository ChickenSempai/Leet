class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        target = amount;
        if (amount == 0)
            return 0;
        int best = INT_MAX;
        best = coinPut(0, coins);
        return best;
    }
    int res = -1;
    int target;
    int coinPut(int sum, vector<int>& coins){
        if (map.find(sum) != map.end())
            return map[sum];
        if (sum == target){
            return 0;
        }
        if (sum < target){
            int best = INT_MAX;
            for(int coin: coins){
                if ((long)sum + coin < INT_MAX){
                    int temp = coinPut(sum + coin, coins);
                    if (temp != -1)
                        best = min(temp, best);
                }
            }
            if (best == INT_MAX)
                map.insert({sum, -1});    
            else
                map.insert({sum, best + 1});
            return map[sum];
        }
        return -1;
    }
    unordered_map <int, int> map;
};