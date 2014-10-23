#include "iostream"
#include "vector"
#include "unordered_map"
#include "BSTStructure.h"
using namespace std;

node* buildHelp(vector<int> a, int start, int end) {
  if(start > end) {
    return NULL;
  }

  if(start == end) {
    return new node(a[start], NULL, NULL);
  }

  int mid = start + (end - start) / 2;

  return new node(a[end], buildHelp(a, start, mid - 1),
                          buildHelp(a, mid + 1, end));
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

node* recoverTreeFromPreOrderAndInorderHelp(const vector<int>& postorder, const vector<int>& inorder, int start, int end, unordered_map<int, int>& m) {
  static int lastPostIndex = postorder.size() - 1;

  // .. not necessary
  //if(start > end)
    //return NULL;

  int rootval = postorder[lastPostIndex--];
  
  if(start == end) {
    return new node(rootval, NULL, NULL);
  }


  //int index = 0;
  //for(int i = start; i <= end; i++)  {
  //  if(inorder[i] == rootval) {
  //    index = i;
  //    break;
  //  }
  //}
  int index = m[rootval];

  node* rightnode = recoverTreeFromPreOrderAndInorderHelp(postorder, inorder, index+1, end, m);
  node* leftnode = recoverTreeFromPreOrderAndInorderHelp(postorder, inorder, start, index-1, m);

  return new node(rootval, leftnode, rightnode);
}

node* recoverTreeFromPostOrderAndInorder(vector<int> postorder, vector<int> inorder) {
  unordered_map<int, int> m;
  for(int i = 0; i < (int)inorder.size(); i++) {
    m[inorder[i]] = i;
  }

  return recoverTreeFromPreOrderAndInorderHelp(postorder, inorder, 0, postorder.size() - 1, m);
}

node* recoverTreeFromPreOrderAndInorderHelp(vector<int>& preorder, vector<int>& inorder, int start, int end, unordered_map<int, int> m) {
  static int preorderIndex = 0;

  int rootval = preorder[preorderIndex++];
  if(start == end)
    return new node(rootval, NULL, NULL);

  int index = m[rootval];
  node* leftnode = recoverTreeFromPreOrderAndInorderHelp(preorder, inorder, start, index - 1, m);
  node* rightnode = recoverTreeFromPreOrderAndInorderHelp(preorder, inorder, index + 1, end, m);

  return new node(rootval, leftnode, rightnode);
}

node* recoverTreeFromPreOrderAndInorder(vector<int>& preorder, vector<int>& inorder) {
 unordered_map<int, int> m;
 for(int i = 0; i < (int)inorder.size(); i++) {
   m[inorder[i]] = i;
 }

 return recoverTreeFromPreOrderAndInorderHelp(preorder, inorder, 0, preorder.size() - 1, m);
}

node* recoverTreeFromPreOrderAndPostorderHelp(vector<int>& preorder, vector<int>& postorder, int start, int end, unordered_map<int, int>& m) {
  static int preorderIndex = 0;

  int rootval = preorder[preorderIndex++];
  int nextval = preorderIndex > (int)preorder.size() - 1 ? -1 : preorder[preorderIndex];

  if(preorderIndex > preorder.size())
    return NULL;

  cout << rootval << " " << nextval << endl;
  if(start == end)
    return new node(rootval, NULL, NULL);

  int nextIdx = m[nextval];
  int rootIdx = m[rootval];

  node* left = recoverTreeFromPreOrderAndPostorderHelp(preorder, postorder, start, nextIdx, m);
  node* right = recoverTreeFromPreOrderAndPostorderHelp(preorder, postorder, nextIdx + 1, rootIdx - 1, m);

  cout << endl;
  cout << "========================" << endl;
  cout << rootval << endl;
  if(left != NULL)
    cout << left->val << endl;
  if(right != NULL)
    cout << right->val << endl;
  cout << "========================" << endl;
  cout << endl;

  return new node(rootval, left, right);
}

node* recoverTreeFromPreOrderAndPostorder(vector<int>& preorder, vector<int>& postorder) {
  unordered_map<int, int> m;
  for(int i = 0; i < (int)postorder.size(); i++) {
    m[postorder[i]] = i;
  }

  return recoverTreeFromPreOrderAndPostorderHelp(preorder, postorder, 0, postorder.size() - 1, m);
}

int main()
{
  vector<int> post = {1, 3, 2, 5, 8, 10, 9, 7, 4};

  vector<int> pre = {4, 2, 1, 3, 7, 5, 9, 8, 10};

  vector<int> in = {1, 2, 3, 4, 5, 7, 8, 9, 10};

  //printBST(buildTreeFromPostOrderTraversal(v));
  printBST(buildBST(in));
  //node* root = recoverTreeFromPostOrderAndInorder(post, in);
  //node* root = recoverTreeFromPreOrderAndInorder(pre, in);
  //node* root = recoverTreeFromPreOrderAndPostorder(pre, post);
  //printBST(recoverTree(v, w));
  //printBST(root);
  return 0;
}
