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


/*
 * Given a binary search tree and a range [low, high], return the sum of all nodes whose
 value falls in that given range
 */
int rangeSum(node* root, int low, int high) {
    if(root == NULL)
        return 0;

    int sum = 0;
    if(root->val > low)
        sum += rangeSum(root->left, low, high);

    if(root->val >= low && root->val <= high)
        sum += root->val;

    if(root->val < high)
        sum += rangeSum(root->right, low, high);

    return sum;
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
    cout << rangeSum(root, 4, 12) << endl;
}
