#include "iostream"
#include "BSTStructure.h"
#include "vector"
using namespace std;

// without extra space, using recursion
node* find(node* root, node* a, node* b) {
  if(root == NULL)
    return NULL;

  if(root == a || root == b)
    return root;

  node* l = find(root->left, a, b);
  node* r = find(root->right, a, b);

  if(l && r)
    return root;

  if(l)
    return l;
  else
    return r;
}


// use extra space
node* find2(node* root, node* a, node* b) {

}




int main()
{
  
  return 0;
}
