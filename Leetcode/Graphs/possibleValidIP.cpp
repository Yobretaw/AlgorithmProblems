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

void findHelp(const string& s, int idx, int part, int pos, string curr, vector<string>& result) {
  if(idx == s.length()) {
    if(part == 3)
      result.push_back(curr);
    return;
  }

  char c = s[idx];
  if(pos == 3) return;
  if(pos == 2 && s[idx - 2] > '2') return;
  if(pos == 2 && s[idx - 2] == '2' && s[idx - 1] > '5') return;
  if(pos == 2 && s[idx - 2] == '2' && s[idx - 1] == '5' && s[idx] > '5') return;
  if(pos == 1 && s[idx - 1] == '0') return;

  if(part == 0 && s.length() - idx <= 3) return;
  if(part == 1 && s.length() - idx <= 2) return;
  if(part == 2 && s.length() - idx <= 1) return;

  curr += s[idx];
  findHelp(s, idx + 1, part, pos + 1, curr, result);
  findHelp(s, idx + 1, part + 1, 0, part == 3 ? curr : curr + ".", result);
}

vector<string> find(const string& s) {
  vector<string> result;
  if(s.length() > 12) return result;
  findHelp(s, 0, 0, 0, "", result);
  return result;
}

int main() {
  //vector<string> res = find("010010");
  vector<string> res = find("19216811");
  for (int i = 0; i < res.size(); ++i) {
    cout << res[i] << endl;
  }
  return 0;
}
