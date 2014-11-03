#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include "BSTStructure.h"
using namespace std;

// ===========================================
// Without extra space, runtime O(n) if the tree is balanced,
// O(n^2) in worst case
// ===========================================
void printLevel(node* root, int level) {
  if(root == NULL)
    return;

  if(level == 0) {
    cout << root->val << endl;
    return;
  }

  printLevel(root->left, level-1);
  printLevel(root->right, level-1);
}

// return the height of the tree
int findHeight(node* root) {
  if(root == NULL)
    return 0;

  return max(findHeight(root->left), findHeight(root->right)) + 1;
}


void printTree(node* root) {
  int height = findHeight(root);

  for (int i = 0; i < height; i++) {
    printLevel(root, i);
  }
}


// ===========================================
// Using a queue, runtime O(n) in all cases(no matter if the tree
// is balanced or not)
// ===========================================
void levelOrderTraversal(node* root) {
  queue<node*> q;
  q.push(root);

  while(!q.empty()) {
    node* curr = q.front();
    q.pop();
    cout << curr->val << endl;

    if(curr->left != NULL)
      q.push(curr->left);
    if(curr->right != NULL)
      q.push(curr->right);
  }
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
  //levelOrderTraversal(root);
  printTree(root);
  return 0;
}
