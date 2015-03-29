#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include "BSTStructure.h"
using namespace std;

bool check(node* root, int& height) {
  if(root == NULL) {
    height = 0;
    return true;
  }

  int lh = 0;
  int rh = 0;
  bool l;
  bool r;
  
  l = check(root->left, lh);
  if(!(l = check(root->left, lh)))
    return 0;
  
  if(!(r = check(root->right, rh)))
    return 0;

  if(abs(lh - rh) >= 2)
    return 0;

  height = (lh > rh) ? lh + 1 : rh + 1;

  return l && r;
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
          new node(14, 
            new node(20, NULL, NULL),
            NULL))));
  
  printBST(root);
  int h;
  cout << check(root, h) << endl;
  return 0;
}
