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

void getNodes(node* root, vector<node*>& nodes);
void detect(pair<node*, node*>& broken, node *prev, node *curr);
/* Two elements of a BST are swapped by mistake.
 *
 * Recover the tree without changing its structure.
 *
 * Note: A solution using O(n) space is pretty straight forward.
 * Could you divise a constant space solution.
 */
//=======================================================
// Space: O(n)
//=======================================================
void recover(node* root) {
  vector<node*> nodes;
  getNodes(root, nodes);

  node *a, *b;
  for (int i = 1; i < nodes.size(); ++i)
    if(nodes[i]->val < nodes[i - 1]->val)
      a = nodes[i];

  for(int i = nodes.size() - 1; i >= 1; --i)
    if(nodes[i]->val < nodes[i - 1]->val)
      b = nodes[i - 1];

  swap(a->val, b->val);
}

void getNodes(node* root, vector<node*>& nodes) {
  if(root == NULL)
    return;

  getNodes(root->left, nodes);
  nodes.push_back(root);
  getNodes(root->right, nodes);
}

//=======================================================
// Space: O(1)
//=======================================================
void recoverMorris(node *root) {
  pair<node*, node*> broken;
  node *prev = NULL;
  node *curr = root;

  while(curr != NULL) {
    if(curr->left == NULL) {
      detect(broken, prev, curr);
      prev = curr;
      curr = curr->right;
    } else {
      node *pred = curr->left;
      while(pred->right != NULL && pred->right != curr)
        pred = pred->right;

      if(pred->right == NULL) {
        pred->right = curr;
        // prev = curr      <-- can't add this line since curr has not been accessed yet
        curr = curr->left;
      } else {
        detect(broken, prev, curr);
        pred->right = NULL;
        prev = curr;
        curr = curr->right;
      }
    }
  }
  swap(broken.first->val, broken.second->val);
}

void detect(pair<node*, node*>& broken, node *prev, node *curr) {
  if(prev != NULL && prev->val > curr->val) {
    if(broken.first == NULL)
      broken.first = prev;
    broken.second = curr;
  }
}

int main() {
  node* root = new node(7, 
      new node(3, 
        new node(13, 
          new node(0, NULL, NULL),
          new node(2, NULL, NULL)),
        new node(5,
          new node(4, NULL, NULL),
          new node(6, NULL, NULL))),
      new node(11,
        new node(9,
          new node(8, NULL, NULL),
          new node(10, NULL, NULL)),
        new node(1,
          new node(12, NULL, NULL),
          new node(14, NULL, NULL))));

  printBST(root);
  recoverMorris(root);
  printBST(root);
  return 0;
}
