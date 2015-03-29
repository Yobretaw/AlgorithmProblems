#include "iostream"
#include "vector"
#include "unordered_map"
#include "BSTStructure.h"
using namespace std;

bool findLevel(node* root, int a, int& level) {
  if(root == NULL)
    return 0;

  if(root->val == a) {
    level++;
    return true;
  }

  if(findLevel(root->left, a, level) || findLevel(root->right, a, level)) {
    level++;
    return true;
  }
  
  return false;
}

bool isSibling(node* root, int a, int b) {
  if(root == NULL)
    return false;

  if(root->left == NULL || root->right == NULL)
    return false;

  if((root->left->val == a && root->right->val == b)
      || (root->right->val == a && root->left->val == b))
    return true;

  return isSibling(root->left, a, b) || isSibling(root->right, a, b);
}

bool check(node* root, int a, int b) {
  int levelA = 0;
  int levelB = 0;

  findLevel(root, a, levelA);
  findLevel(root, b, levelB);

  if(levelA != levelB) {
    return false;
  }

  if(isSibling(root, a, b)) {
    return false;
  }
  
  return true;
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
  cout << check(root, 2, 14) << endl;
  return 0;
}
