#include "iostream"
#include "queue"
#include "vector"
#include "map"
#include "unordered_set"
#include "unordered_map"
using namespace std;

int BFS(string start, string end, vector<string> dict) {
  queue<string> q; 
  map<string, int> seen;

  int word_len = dict.size() == 0 ? 0 : dict[0].size();

  map<string, vector<string> > table; 
  for(auto curr: dict) {
    for(int j = 0; j < curr.length(); j++) {
      string s = curr;
      s[j] = '*';
      table[s].push_back(curr);
    }
  }

  int len = INT_MAX;
  int level = 0;

  // used to track the parent of a string
  unordered_map<string, string> parent;

  q.push(start);
  while(q.size() != 0) {
    string curr = q.front();
    level = seen[curr];
    q.pop();

    //cout << curr << endl;
    if(curr == end) len = min(len, level);

    for(int i = 0; i < word_len; i++) {
      char tmp = curr[i];
      string t = curr;
      curr[i] = '*';

      if(table[curr].size() == 0) continue;

      for(auto next : table[curr]) {
        if(seen[next] || next == start) continue;

        q.push(next);
        seen[next] = level + 1;
        parent[next] = t;
      }
      // swap back
      curr[i] = tmp;
    }
  }

  // printing path
  vector<string> path;
  if(len != INT_MAX) {
    while(end != start) {
      path.insert(path.begin(), 1, end);
      end = parent[end];
    }
    path.insert(path.begin(), 1, start);
    for (auto s : path) {
      cout << s << endl;
    }
  }
  return len == INT_MAX ? 0 : len + 1;
}

int ladder(string start, string end, unordered_set<string>& dict) {
  vector<string> d;
  for(auto w : dict) {
    d.push_back(w);
  }
  return BFS(start, end, d);
}

int main()
{
  string start = "hit";
  string end = "cog";
  unordered_set<string> dict = {"hot", "hat", "cog", "dot", "dog", "hit", "lot", "aog", "log"};

  cout << ladder(start, end, dict) << endl;
  return 0;
}
