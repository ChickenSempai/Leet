class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int temp;
        for (int j = 0; j < matrix.size() / 2; j++) {
            for (int i = j; i < matrix.size() - j - 1; i++) {
                temp = matrix[j][i];
                matrix[j][i] = matrix[matrix.size() - i-1][j];
                matrix[matrix.size() - i-1][j] = matrix[matrix.size() - j-1][matrix.size() - i-1];
                matrix[matrix.size() - j-1][matrix.size() - i-1] = matrix[i][matrix.size() - j-1];
                matrix[i][matrix.size() - j-1] = temp;
            }
        }
        
    }

};
