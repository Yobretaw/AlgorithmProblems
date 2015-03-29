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

int eval(int a, int b, string op);

/* Evaluate the value of an arthimetic expression in 
 * Reverse Polish Notation.
 *
 * Valid operator are +, -, *, /. Each oeprand may be
 * an integer or another expression.
 * 
 * Some example:
 *
 * ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 * 
 * ["4", "13", "5" "/", "+"] -> (4 + (13 / 5)) -> 6
 */
int evaluate(const vector<string>& exp) {
  if(exp.size() == 0) return 0;

  stack<int> s;
  int a, b;
  for (int i = 0; i < exp.size(); ++i) {
    if(exp[i] == "+" ||
        exp[i] == "-" ||
        exp[i] == "*" ||
        exp[i] == "/") {
      b = s.top(); s.pop();
      a = s.top(); s.pop();
      s.push(eval(a, b, exp[i]));
    } else {
      int val = atoi((char*)exp[i].c_str());
      s.push(val);
    }
  }
  return s.top();
}

int eval(int a, int b, string op) {
  if(op == "+") return a + b;
  if(op == "-") return a - b;
  if(op == "*") return a * b;
  if(op == "/") return a / b;

  return 0;
}

bool is_operator(const string& op) {
  return op.size() == 1 && string("+-*/").find(op) != string::npos;
}


// recursive way
int eval2(vector<string>& tokens) {
  int x, y;
  string token = tokens.back(); tokens.pop_back();
  if(is_operator(token)) {
    y = eval2(tokens);
    x = eval2(tokens);

    if(token[0] == '+') x += y;
    if(token[0] == '-') x -= y;
    if(token[0] == '*') x *= y;
    if(token[0] == '/') x /= y;
  } else {
    size_t i;
    x = stoi(token, &i);
  }
  return x;
}

int main() {
  vector<string> v = { "7", "3", "/" };
  cout << eval2(v) << endl;
  return 0;
}
