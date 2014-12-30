#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include "BSTStructure.h"
using namespace std;

void insert(node *root, node *n) {
  if(root->val > n->val) {
    if(root->left == NULL) {
      root->left = n;
      return;
    }
    insert(root->left, n);
  } else {
    if(root->right == NULL) {
      root->right = n;
      return;
    }
    insert(root->right, n);
  }
}

node* insert(node* root, node *n) {
  if(root == NULL)
    return n;

  insert(root, n);
  return root;
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
        new node(14,
          new node(13, NULL, NULL),
          new node(15, NULL, NULL))));
  printBST(root);
  insert(root, new node(12, NULL, NULL));
  printBST(root);
  return 0;
}
