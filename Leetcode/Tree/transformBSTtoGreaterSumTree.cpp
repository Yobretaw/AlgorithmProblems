#include <iostream>
#include "BSTStructure.h"
using namespace std;

/*
 *
 *            _______7______
 *           /              \
 *        ___3__          __11__
 *       /      \        /      \
 *      _1      _5      _9      13
 *     /  \    /  \    /  \    /  \
 *     0   2   4   6   8  10  12  14
 *
 *
 *                | |
 *                \/
 *
 *            ______77______
 *           /              \
 *        __99__          __39__
 *       /      \        /      \
 *      104      90      60      14
 *     /  \    /  \    /  \    /  \
 *    105 102  95  84  69  50  27   0
 *
 *
 */

void transform(node* root, int& sum) {
  if(root == NULL) return;

  transform(root->right, sum);

  int tmp = root->val;
  root->val = sum;
  sum += tmp;

  transform(root->left, sum);
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
  int sum = 0;
  transform(root, sum);
  printBST(root);
  return 0;
}

