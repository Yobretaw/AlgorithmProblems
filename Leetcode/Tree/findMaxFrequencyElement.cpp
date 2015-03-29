#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include "BSTStructure.h"
#include <unordered_map>
using namespace std;

int findMin(node *root) {
  while(root->left != NULL)
    root = root->left;

  return root->val;
}

//===========================================================================
//                      Find Element that appears most times
//===========================================================================
// Given a bst, find the lement that appeats most times. No extra space
// allowed
void findHelp(node* root, int& maxVal, int& maxCount, int& currVal, int& currCount) {
  if(root == NULL)
    return;

  findHelp(root->left, maxVal, maxCount, currVal, currCount);

  if(root->val == maxVal) {
    maxCount++;
  } else {
    if(root->val == currVal) {
      currCount++;
    } else {
      currVal = root->val;
      currCount = 1;
    }

    if(currCount > maxCount) {
      maxCount = currCount;
      maxVal = root->val;
    }
  }

  findHelp(root->right, maxVal, maxCount, currVal, currCount);
}

int findMaxFreqElement(node *root) {
  if(root == NULL)
    return 0;

  int maxVal = findMin(root) - 1;
  int maxCount = 0;
  int currVal = maxVal;
  int currCount = 0;
  findHelp(root, maxVal, maxCount, currVal, currCount);

  return maxVal;
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
  cout << findMaxFreqElement(root) << endl;
  return 0;
}
