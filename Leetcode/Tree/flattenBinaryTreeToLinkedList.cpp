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


void flatten_help(node* root, node*& prev, node*& head);
node *flatten2_help(node *root, node *tail);

/* Given a binary tree, flatten it to a linked list in-place.
 *
 * For example, given
 *
 *      4
 *     / \
 *    2   5
 *   / \   \
 *  1   3   6
 *  
 * The flattened tree should look like:
 *  
 *  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
 */

node* flatten(node *root) {
  node *prev = NULL;
  node *head = NULL;
  flatten_help(root, prev, head);
  return head;
}

void flatten_help(node* root, node*& prev, node*& head) {
  if(root == NULL)
    return;

  if(prev == NULL)
    head = root;
  else
    prev->right = root;

  flatten_help(root->left, prev, head);

  root->left = prev;
  prev = root;
  head->left = root;
  
  node *right = root->right;
  root->right = head;
  flatten_help(right, prev, head);
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
  node *head = flatten(root);
  node *tmp = head;
  do {
    cout << head->val << endl;
    head = head->left;
  } while(head != tmp);
  return 0;
}
