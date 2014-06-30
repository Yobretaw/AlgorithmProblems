#include "iostream"
#include "BSTStructure.h"
using namespace std;

void traversal(node* root);
void moveToRight(node* root);

int main()
{
  node* n1 = makeBST(1, NULL, NULL);
  node* n3 = makeBST(3, NULL, NULL);
  node* n2 = makeBST(2, n1, n3);
  node* n5 = makeBST(5, NULL, NULL);
  node* n4 = makeBST(4, n2, n5);
  traversal(n4);

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
