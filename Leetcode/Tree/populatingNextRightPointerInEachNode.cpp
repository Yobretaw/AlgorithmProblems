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

void connectPerfectBST_help(node *root, node *sibling);

/* Given the following binary tree,
 *
 *      1
 *     / \
 *    2   3
 *   / \   \
 *  4   5   7
 *  
 *      1 -> NULL
 *     / \
 *    2 ->3 -> NULL
 *   / \   \
 *  4 ->5 ->7 -> NULL
 */
void connect(node *root) {
  node *head = root;
  node *curr = NULL;
  node *prev = NULL;

  while(head) {
    curr = head;
    head = prev = NULL;

    while(curr != NULL) {
      if(curr->left != NULL) {
        if(prev != NULL) prev = prev->next = curr->left;
        else head = prev = curr->left;
      }
      if(curr->right != NULL) {
        if(prev != NULL) prev = prev->next = curr->right;
        else head = prev = curr->right;
      }
      curr = curr->next;
    }
  }
}

void connectPerfectBST(node *root) {
  connectPerfectBST_help(root, NULL);
}

void connectPerfectBST_help(node *root, node *sibling) {
  if(root == NULL)
    return;
  else
    root->next = sibling;

  connectPerfectBST_help(root->left, root->right);
  connectPerfectBST_help(root->right, sibling == NULL ? NULL : sibling->left);
}

int main() {
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
  connect(root);
  //connectPerfectBST(root);
  while(root != NULL) {
    node *head = root;
    while(head != NULL) {
      cout << head->val << " ";
      head = head->next;
    }
    cout << endl;
    root = root->left;
  }
  return 0;
}
