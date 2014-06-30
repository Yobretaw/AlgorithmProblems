#include "iostream"
#include "stack"
#include "BSTStructure.h"
using namespace std;

void traversal(node* root);
void pushLeft(stack<node*>& s, node* root);

int main()
{
  //node* root = makeBST(2, makeBST(1, NULL, NULL), makeBST(3, NULL, NULL));
  node* n1 = makeBST(1, NULL, NULL);
  node* n3 = makeBST(3, NULL, NULL);
  node* n2 = makeBST(2, n1, n3);
  node* n5 = makeBST(5, NULL, NULL);
  node* n4 = makeBST(4, n2, n5);
  traversal(n4);
  return 0;
}


void traversal(node* root) {
  if (root == NULL) {
    return;
  }

  stack<node*> s;
  pushLeft(s, root);

  while(s.size() != 0) {
    node* curr = s.top();
    s.pop();

    cout << curr->val << endl;
    curr = curr->right;
    pushLeft(s, curr);
  }
}

void pushLeft(stack<node*>& s, node* root) {
  while(root != NULL) {
    s.push(root);
    root = root->left;
  }
}
