#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
#include "BSTStructure.h"
using namespace std;

void traversal_help(node* root, int level, vector<vector<int> >& result);

/* Given a binary tree, return the zigzag level order traversal of its nodes'
 * values. (i.e, from left to right, then right to left for the next level and
 * alternate between).
 * 
 * For example: given binary tree 
 * 
 *      3
 *    /  \
 *   9   20
 *      /  \
 *     15   7
 *     
 * return its zigzag level order traversal as:
 * [
 *  [3],
 *  [20, 9],
 *  [15, 7]
 * ]
 * 
 */
//==================================================
// O(n) time, O(n) *extra* space
//==================================================
void zigzagTraversal(node *root) {
  vector<vector<int> > result;
  traversal_help(root, 1, result);

  for (int i = 0; i < result.size(); ++i)
    for (int j = 0; j < result[i].size(); ++j)
      cout << result[i][j] << endl;
}

void traversal_help(node* root, int level, vector<vector<int> >& result) {
  if(root == NULL)
    return;

  if(level > result.size())
    result.push_back(vector<int>());

  if(level % 2 == 1)
    result[level - 1].push_back(root->val);
  else
    result[level - 1].insert(result[level - 1].begin(), root->val);

  traversal_help(root->left, level + 1, result);
  traversal_help(root->right, level + 1, result);
}

//==================================================
// O(n) time, O(n) *extra* space
//==================================================
void zigzagTraversal2(node* root) {
  vector<vector<int> > result;
  if(root == NULL)
    return;

  queue<node*> q;
  vector<int> level;
  bool left_to_right = true;

  q.push(root);
  q.push(NULL);
  while(!q.empty()) {
    node *curr = q.front();
    q.pop();
    if(curr) {
      level.push_back(curr->val);
      if(curr->left) q.push(curr->left);
      if(curr->right) q.push(curr->right);
    } else {
      if(left_to_right) {
        result.push_back(level);
      } else {
        reverse(level.begin(), level.end());
        result.push_back(level);
      }
      level.clear();
      left_to_right = !left_to_right;

      if(q.size() > 0) q.push(NULL);  // push separator
    }
  }

  for (int i = 0; i < result.size(); ++i)
    for (int j = 0; j < result[i].size(); ++j)
      cout << result[i][j] << endl;
}

int main() {
  node* root = new node(7, 
      new node(3, 
        new node(1, 
          new node(0, NULL, NULL),
          new node(2, NULL, NULL)),
        new node(5,
          new node(4, NULL, NULL),
          new node(6, NULL, NULL))),
      new node(11,
        new node(9,
          new node(8, NULL, NULL),
          new node(10, NULL, NULL)),
        new node(13,
          new node(12, NULL, NULL),
          new node(14, NULL, NULL))));

  printBST(root);
  zigzagTraversal2(root);
  return 0;
}
