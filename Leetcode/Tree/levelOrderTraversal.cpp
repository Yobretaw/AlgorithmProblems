#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include "BSTStructure.h"
using namespace std;

void traversal_help(node *root, int level, vector<vector<int> >& result);

// ===============================================================
// Using a queue, runtime O(n) in all cases(no matter if the tree
// is balanced or not)
// ===============================================================
void levelOrderTraversal(node* root) {
  queue<node*> q;
  q.push(root);

  while(!q.empty()) {
    node* curr = q.front();
    q.pop();
    cout << curr->val << endl;

    if(curr->left != NULL)
      q.push(curr->left);
    if(curr->right != NULL)
      q.push(curr->right);
  }
}


// ===============================================================
// Without extra space, runtime O(n) if the tree is balanced,
// O(n^2) in worst case
// ===============================================================
void printLevel(node* root, int level) {
  if(root == NULL)
    return;

  if(level == 0) {
    cout << root->val << endl;
    return;
  }

  printLevel(root->left, level-1);
  printLevel(root->right, level-1);
}

// return the height of the tree
int findHeight(node* root) {
  if(root == NULL)
    return 0;

  return max(findHeight(root->left), findHeight(root->right)) + 1;
}


void levelOrderTraversal2(node* root) {
  int height = findHeight(root);

  for (int i = 0; i < height; i++) {
    printLevel(root, i);
  }
}

// ===============================================================
// O(n) time, O(n) space
// ===============================================================
void levelOrderTraversal3(node *root) {
  vector<vector<int> > result;
  traversal_help(root, 1, result);
  for (int i = 0; i < result.size(); ++i)
    for (int j = 0; j < result[i].size(); ++j) 
      cout << result[i][j] << endl;
}

void traversal_help(node *root, int level, vector<vector<int> >& result) {
  if(root == NULL)
    return;

  if(level > result.size())
    result.push_back(vector<int>());

  result[level - 1].push_back(root->val);
  traversal_help(root->left, level + 1, result);
  traversal_help(root->right, level + 1, result);
}

int main()
{
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
  //levelOrderTraversal(root);
  //levelOrderTraversal2(root);
  levelOrderTraversal3(root);
  return 0;
}
