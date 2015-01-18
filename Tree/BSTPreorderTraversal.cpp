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

/* Traverse the given BST without using recursion
 */
vector<int> preorderTraversalWithStack(node *root) {
  vector<int> result;
  stack<node*> s;

  if(root != NULL) s.push(root);

  while(!s.empty()) {
    root = s.top();
    s.pop();
    result.push_back(root->val);

    if(root->right != NULL) s.push(root->right);
    if(root->left != NULL) s.push(root->left);
  }
  return result;
}

vector<int> preorderTraversalMorris(node *root) {
  vector<int> result;
  node *curr = root;

  while(curr != NULL) {
    if(curr->left == NULL) {
      result.push_back(curr->val);
      curr = curr->right;
    } else {
      // find its predecessor
      node *pred = curr->left;
      while(pred->right != NULL && pred->right != curr)
        pred = pred->right;
      
      if(pred->right == NULL) {
        // not yet serialized, serialize it
        result.push_back(curr->val);
        pred->right = curr;
        curr = curr->left;
      } else {
        // recover from serialization
        pred->right = NULL;
        curr = curr->right;
      }
    }
  }
  return result;
}

int main() {
  node* n1 = new node(1, NULL, NULL);
  node* n3 = new node(3, NULL, NULL);
  node* n2 = new node(2, n1, n3);
  node* n6 = new node(6, NULL, NULL);
  node* n7 = new node(7, NULL, NULL);
  node* n5 = new node(5, n6, n7);
  node* n4 = new node(4, n2, n5);
  printBST(n4);

  //vector<int> result = preorderTraversalWithStack(n4);
  vector<int> result = preorderTraversalMorris(n4);
  for (int i = 0; i < result.size(); ++i) {
    cout << result[i] << endl;
  }
  return 0;
}
