#include "iostream"
#include "BSTStructure.h"
#include <climits>
using namespace std;

//Given a binary tree in which each node element contains a number. 
//Find the maximum possible sum from one leaf node to another.


int findHelp(node* root, int& max) {
  if(root == NULL)
    return 0;

  int left = findHelp(root->left, max);
  int right = findHelp(root->right, max);

  int currMax = left + right + root->val;
  if(currMax > max && root->left && root->right)
    max = currMax;

  return root->val + ((left > right) ? left : right);
}

int find(node* root) {
  int max = INT_MIN;
  findHelp(root, max);
  return max;
}

int main() {
  node* root = new node(-15,
      new node(5,
        new node(-8,
          new node(2, NULL, NULL),
          new node(6, NULL, NULL)),
        new node(1, NULL, NULL)),
      new node(6, 
        new node(3, NULL, NULL),
        new node(9, NULL,
          new node(0,
            new node(4, NULL, NULL),
            new node(-1, 
              new node(10, NULL, NULL),
              NULL)))));
  
  node* root2 = new node(-400,
      new node(-900,
        new node(-800,
          new node(-600, NULL, NULL),
          new node(-200, NULL, NULL)),
        NULL),
      new node(-200,
          new node(-903, NULL, NULL),
          new node(40, NULL,
            new node(40, NULL, NULL))));

  printBST(root);
  cout << find(root) << endl;
  printBST(root2);
  cout << find(root2) << endl;
}
