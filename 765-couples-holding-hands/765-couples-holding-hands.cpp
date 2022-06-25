class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        std::vector<int> seatind(60);
        for(int i = 0; i < row.size(); i++)
            seatind[row[i]] = i;
        size_t swaps = 0;
        for(int i = 0; i < row.size(); i+=2){
            int tofind;
            if (row[i]%2)
                tofind = row[i]-1;
            else
                tofind = row[i]+1;
            if (row[i+1] != tofind){
                int temp = row[i+1];
                std::swap(row[i+1], row[seatind[tofind]]);
                std::swap(seatind[tofind], seatind[temp]);
                swaps += 1;
            }
        }
        return swaps;
    }
};