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

static void reverse(node *from, node *to);
static void visit_reverse(node *from, node *to, function<void(const node*)>& visit);

/* Given a binary tree, return the postorder traversal of its nodes'
 * value.
 *
 * Do not use recursion.
 */
vector<int> postOrderTraversalWithStack(node *root) {
  vector<int> result;
  stack<node*> s;
  node *curr, *prev;

  curr = root;
  do {
    while(curr != NULL) {
      s.push(curr);
      curr = curr->left;
    }

    prev = NULL;
    while(!s.empty()) {
      curr = s.top();
      s.pop();

      // curr has no right child or its right child has already been accessed,
      // access curr.
      if(curr->right == prev) {
        result.push_back(curr->val);
        prev = curr;  // save the node(i.e curr) we have just accessed
      } else {
        // curr can't be accessed right now, push it to stack,
        // and handle its right child first
        s.push(curr);
        curr = curr->right;
        break;
      }
    }
  } while(!s.empty());
  return result;
}

vector<int> postOrderTraversalMorris(node *root) {
  vector<int> result;
  node dummy;
  node *curr, *prev = NULL;

  // lamda function
  function<void(const node*)> visit = [&result](const node* n) {
    result.push_back(n->val);
  };

  dummy.left = root;
  curr = &dummy;
  while(curr != NULL) {
    if(curr->left == NULL) {
      prev = curr;
      curr = curr->right;
    } else {
      node *pred = curr->left;
      while(pred->right != NULL && pred->right != curr)
        pred = pred->right;

      if(pred->right == NULL) {
        pred->right = curr;
        prev = curr;
        curr = curr->left;
      } else {
        visit_reverse(curr->left, prev, visit);
        prev->right = NULL;
        prev = curr;
        curr = curr->right;
      }
    }
  }

  return result;
}

// reverse the path between 'from' and 'to'
static void reverse(node *from, node *to) {
  node *x = from, *y = from->right, *z;
  if(from == to) return;

  while(x != to) {
    z = y->right;
    y->right = x;
    x = y;
    y = z;
  }
}

// push all nodes in the path to result
static void visit_reverse(node *from, node *to, function<void(const node*)>& visit) {
  node *p = to;
  reverse(from, to);

  while(true) {
    visit(p);
    if(p == from)
      break;
    p = p->right;
  }
  reverse(to, from);
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

  //vector<int> result = postOrderTraversalWithStack(n4);
  vector<int> result = postOrderTraversalMorris(n4);
  for (int i = 0; i < result.size(); ++i) {
    cout << result[i] << endl;
  }
  return 0;
}
