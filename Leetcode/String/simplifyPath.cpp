#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
using namespace std;

/* "/a/./b/../../c/", => { "a", ".", "b", ""}
 */
vector<string> getElements(const string& s) {
  vector<string> result;

  for (int i = 0; i < s.length(); ++i) {
    if(s[i] == '/') continue;

    string curr = "";
    int j;
    for (j = i; j < s.length() && s[j] != '/'; ++j)
      curr += s[j];
    
    result.push_back(curr);
    i = j;
  }

  return result;
}

/* Given an absolute path for a file(Unix-style), simplify it.
 * 
 * For example:
 *    "/home/" => "/home"
 *    "/a/./b/../../c/", => "/c"
 *
 *    "/../" => "/"
 *    "/home//foo/" => "/home/foo"
 *    
 *    idea: use a stack
 */
string simplify(string path) {
  stack<string> s;
  vector<string> elements = getElements(path);

  for (int i = 0; i < elements.size(); ++i) {
    if(elements[i] == ".") continue;
    else if(elements[i] == "..") {
      if(s.size() != 0)
        s.pop();
    }
    else s.push(elements[i]);
  }

  if(s.size() == 0)
    return "/";

  string result = s.top();
  s.pop();
  while(!s.empty()) {
    result = s.top() + "/" + result;
    s.pop();
  }

  return "/" + result;
}


int main() {
  string path = "/a/./b/../../c/";
  //string path = "/home/";
  //string path = "/../";
  //string path = "/home//foo/";
  cout << simplify(path) << endl;
  return 0;
}
