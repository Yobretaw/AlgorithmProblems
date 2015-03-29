#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include "BSTStructure.h"
#include <unordered_map>
using namespace std;

bool isBalanced_help(node *root, int& depth) {
  if(root == NULL) return true;

  int lh = 0, rh = 0;
  if(!isBalanced_help(root->left, lh)) return false;
  if(!isBalanced_help(root->right, rh)) return false;
  if(abs(lh - rh) > 1) return false;

  depth = max(lh, rh) + 1;
  
  return true;
}

/* Given a binary tree, determine if it's height-balanced
 */
bool isBalanced(node* root) {
  int depth = 0;
  return isBalanced_help(root, depth);
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
          new node(14, 
            new node(20, NULL, NULL),
            NULL))));
  printBST(root);
  cout << isBalanced(root) << endl;
  return 0;
}
