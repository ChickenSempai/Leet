/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::queue<TreeNode*> fifo;
        if (root != nullptr)
            fifo.push(root);
        std::vector<vector<int>> res;
        size_t level = -1;
        size_t fifopack = 0;
        while(!fifo.empty()){
            if (fifopack==0){
                res.push_back({});
                ++level;
                fifopack = fifo.size();
            }
            auto *popped = fifo.front();
            fifopack--;
            // std::cout << popped->val;
            res[level].push_back(popped->val);
            if (popped->left)
                fifo.push(popped->left);
            if (popped->right)
                fifo.push(popped->right);
            fifo.pop();
        }
        return res;
    }
};