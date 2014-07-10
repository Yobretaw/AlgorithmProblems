#include <iostream>
using namespace std;

bool isSubtree(node* root, node* tr) {
  if(root == NULL)
    return false;

  return isRootHere(root, tr) || isSubtree(root->left, tr) || isSubtree(root->right, tr);
}


bool isRootHere(node* root, node* tr) {
  if(root == NULL && tr == NULL)
    return true;

  if(root == NULL || tr == NULL)
    return false;

  if(root->val != tr->val)
    return false;

  return isRootHere(root->left, tr->left) && isRootHere(root->right, tr->right);
}
