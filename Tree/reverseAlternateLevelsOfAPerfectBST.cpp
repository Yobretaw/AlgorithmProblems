#include "iostream"
#include "vector"
#include "stack"
#include "map"
#include "BSTStructure.h"
using namespace std;
/*
 *
 *  Given tree: 
 *               a
 *            /     \
 *           b       c
 *         /  \     /  \
 *        d    e    f    g
 *       / \  / \  / \  / \
 *      h  i j  k l  m  n  o 
 *
 *  Modified tree:
 *  	           a
 *            /     \
 *           c       b
 *         /  \     /  \
 *        d    e    f    g
 *       / \  / \  / \  / \
 *      o  n m  l k  j  i  h 
 *
 */

void reverse(node* root, stack<int>& v, int level, bool isFirst);

int main()
{
  stack<int> v;
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
  reverse(root, v, 0, true);
  reverse(root, v, 0, false);
  printBST(root);
  return 0;
}

void reverse(node* root, stack<int>& v, int level, bool isFirst) {
  if(root == NULL) return;

  // inorder traversal
  reverse(root->left, v, level+1, isFirst);
  if(isFirst) {
    v.push(root->val);
  } else {
    root->val = v.top();
    v.pop();
  }
  reverse(root->right, v, level+1, isFirst);
  return;
}
