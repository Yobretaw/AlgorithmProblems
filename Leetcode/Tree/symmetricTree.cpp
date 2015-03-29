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

bool isSymmetric_help(node *left, node *right);


bool isSymmetric(node *root) {
  return root ? isSymmetric_help(root->left, root->right) : true;
}

bool isSymmetric_help(node *left, node *right) {
  if(left == NULL && right == NULL) return true;
  if(left == NULL || right == NULL) return false;

  return left->val == right->val
    && isSymmetric_help(left->right, right->left)
    && isSymmetric_help(left->left, right->right);
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
      new node(3, 
        new node(5,
          new node(6, NULL, NULL),
          new node(4, NULL, NULL)),
        new node(1, 
          new node(2, NULL, NULL),
          new node(0, NULL, NULL))));

  printBST(root);
  cout << isSymmetric(root) << endl;
  return 0;
}
