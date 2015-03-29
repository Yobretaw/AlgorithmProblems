#include "iostream"
#include "stack"
#include "BSTStructure.h"
using namespace std;

void traversal(node* root);
void pushLeft(stack<node*>& s, node* root);
void postTraversal(node*);

int main()
{
  node* n1 = new node(1, NULL, NULL);
  node* n3 = new node(3, NULL, NULL);
  node* n2 = new node(2, n1, n3);
  node* n6 = new node(6, NULL, NULL);
  node* n7 = new node(7, NULL, NULL);
  node* n5 = new node(5, n6, n7);
  node* n4 = new node(4, n2, n5);
  printBST(n4);
  postTraversal(n4);
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

    // if inorder traversal, uncomment the line below
    cout << curr->val << endl;
    curr = curr->right;
    pushLeft(s, curr);
  }
}

void pushLeft(stack<node*>& s, node* root) {
  while(root != NULL) {
    // if preorder traversal, uncomment the linw below
    //cout << root->val << endl;
    s.push(root);
    root = root->left;
  }
}

void postTraversal(node* root) {
  stack<node*> s;

  do {
    while(root != NULL) {
      if(root->right)
        s.push(root->right);

      s.push(root);
      root = root->left;
    }

    root = s.top();
    s.pop();

    if(root->right != NULL && s.size() != 0 && root->right == s.top()) {
      s.pop();
      s.push(root);
      root = root->right;
    } else {
      cout << root->val << endl;
      root = NULL;
    }
  } while(s.size() != 0);
}
