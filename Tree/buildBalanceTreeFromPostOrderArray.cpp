#include "iostream"
#include "vector"
#include "BSTStructure.h"
using namespace std;

node* buildHelp(vector<int> a, int start, int end) {
  if(start > end) {
    return NULL;
  }

  if(start == end) {
    return new node(a[start], NULL, NULL);
  }

  int newend = (start + end - 1) / 2;
  int newstart = newend + 1;

  return new node(a[end], buildHelp(a, start, newend),
                          buildHelp(a, newstart, end - 1));
}

node* buildTreeFromPostOrderTraversal(vector<int> a) {
  return buildHelp(a, 0, a.size() - 1);
}


node* buildBSTHelp(vector<int> a, int start, int end) {
  if(start > end)
    return NULL;

  if(start == end)
    return new node(a[start], NULL, NULL);

  int mid = (start + end) / 2;
  return new node(a[mid], buildBSTHelp(a, start, mid - 1),
                          buildBSTHelp(a, mid + 1, end));
}

node* buildBST(vector<int> a) {
  return buildBSTHelp(a, 0, a.size() - 1);
}

node* recoverTreeHelp(vector<int> postorder, vector<int> inorder, int start, int end, int& min) {
  static int lastPostIndex = postorder.size() - 1;
  if(start > end)
    return NULL;

  int rootval = postorder[lastPostIndex--];
  
  if(start == end) {
    return new node(rootval, NULL, NULL);
  }


  int index = 0;
  for(int i = start; i <= end; i++)  {
    if(inorder[i] == rootval) {
      index = i;
      break;
    }
  }

  node* rightnode = recoverTreeHelp(postorder, inorder, index+1, end, min);
  node* leftnode = recoverTreeHelp(postorder, inorder, start, index - 1, min);
  return new node(rootval, leftnode, rightnode);
}

node* recoverTree(vector<int> postorder, vector<int> inorder) {
  int min = inorder.size() - 1;
  return recoverTreeHelp(postorder, inorder, 0, postorder.size() - 1, min);
}

int main()
{
  vector<int> v;
  v.push_back(1);
  v.push_back(3);
  v.push_back(5);
  v.push_back(4);
  v.push_back(2);

  vector<int> w;
  w.push_back(1);
  w.push_back(2);
  w.push_back(3);
  w.push_back(4);
  w.push_back(5);

  //printBST(buildTreeFromPostOrderTraversal(v));
  //printBST(buildBST(v));
  //recoverTree(v, w);
  printBST(recoverTree(v, w));
  return 0;
}
