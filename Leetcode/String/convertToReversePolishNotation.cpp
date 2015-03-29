#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

string convert(string s) {
  stack<string> st;

  for (int i = 0; i < s.length(); i++) {
    if(s[i] == '(')
      continue;
    if(s[i] == ')') {
      string post = st.top();
      st.pop();
      string op = st.top();
      st.pop();
      string pre = st.top();
      st.pop();

      st.push(pre + post + op);
    } else {
      string curr;
      stringstream  ss;
      ss << s[i];
      ss >> curr;
      st.push(curr);
    }
  }

  return st.top();
}

int main() {
  // should output: at+bac++cd+^*
  cout << convert("((a+t)*((b+(a+c))^(c+d)))") << endl;
  return 0;
}
