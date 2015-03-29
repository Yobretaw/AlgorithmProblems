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

int sumPath_help(node *root, int sum);
/* Given a binary tree containing digits from 0-9 only, each root-to-leaf
 * could represent a number.
 *
 * An example is the root-to-leaf path 1->2->3 which represents the number
 * 123.
 * 
 * Find the total sum of all root-to-leaf numbers.
 *
 * For example,
 *
 *    1
 *   / \
 *  2   3
 *
 * The root-to-leaf path 1->2 represents the number 12, and the root-to-leaf
 * 1->3 represents the number 13. Your function should return 12 + 13 = 25
 */
int sumPath(node *root) {
  return sumPath_help(root, 0);
}

int sumPath_help(node *root, int sum) {
  if(root == NULL)
    return 0;

  if(root->left == NULL && root->right == NULL)
    return sum * 10 + root->val;

  return sumPath_help(root->left, sum * 10 + root->val) + sumPath_help(root->right, sum * 10 + root->val);
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
      new node(1,
        new node(9,
          new node(8, NULL, NULL),
          new node(0, NULL, NULL)),
        new node(3,
          new node(2, NULL, NULL),
          new node(4, NULL, NULL))));
  printBST(root);
  cout << sumPath(root) << endl;
  return 0;
}
