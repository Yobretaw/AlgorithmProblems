#include "iostream"
#include "BSTStructure.h"
using namespace std;

node* find(node* root) {
  if(root == NULL)
    return NULL;

  if(root->left == NULL && root->right == NULL)
    return NULL;

  if(root->right == NULL) {
    root = root->left;
    while(root->right != NULL)
      root = root->right;

  } else {
    while(root->right->right != NULL) {
      root = root->right;
    }
  }

  return root;
}

int main()
{
  return 0;
}
