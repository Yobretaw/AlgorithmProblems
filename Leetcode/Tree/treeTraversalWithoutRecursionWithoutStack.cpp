#include "iostream"
#include "BSTStructure.h"
using namespace std;

void traversal(node* root);
void moveToRight(node* root);

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
  traversal(root);
  return 0;
}

void traversal(node* root) {
  node *curr = root;
  node *pre;
  while(curr != NULL) {
    if (curr->left == NULL) {
      cout << curr->val << endl;
      curr = curr->right;
    } else {
      /* Find the inorder predecessor of current */
      pre = curr->left;
      while(pre->right != NULL && pre->right != curr) {
        pre = pre->right;
      }
      /* Make current as right child of its inorder predecessor */
      if (pre->right == NULL) {
        pre->right = curr;
        curr = curr->left;
      } else {
        /* revert the changes made in if part to restore the 
         * original tree. i.e, fix the right child of predecessor
         */
        pre->right = NULL;
        cout << curr->val << endl;
        curr = curr->right;
      }
    }
  }
}
