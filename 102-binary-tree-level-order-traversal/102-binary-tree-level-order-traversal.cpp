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
        while(!fifo.empty()){
            size_t cursize = fifo.size();
            std::vector<int> temp;
            while(cursize-- > 0){
                auto *popped = fifo.front();
                temp.push_back(popped->val);
                if (popped->left)
                    fifo.push(popped->left);
                if (popped->right)
                    fifo.push(popped->right);
                fifo.pop();
            }
            res.push_back(temp);
            temp.clear();
        }
        return res;
    }
};