#include <iostream>
#include <vector>
#include <stack>
#include "BSTStructure.h"
using namespace std;

node* buildBST(const vector<int>& a) {
  if(a.size() == 0)
    return NULL;

  if(a.size() == 1)
    return new node(a[0], NULL, NULL);

  stack<node*> s;
  int start = 0, end = a.size() - 1;
  int mid = (start + end) / 2;
  node* root = new node(a[mid], NULL, NULL);
  s.push(root);

  end = mid - 1;
  while(!s.empty()) {
  }

  return root;
}

int main()
{
  
  return 0;
}
