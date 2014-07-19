#include "iostream"
#include "queue"
#include "vector"
#include "map"
using namespace std;

bool BFS(string start, string end, vector<string> dict) {
  queue<string> q; 
  map<string, bool> seen;

  map<string, vector<string> > table; 
  for(int i = 0; i < (int)dict.size(); i++) {
    for(int j = 0; j < (int)start.length(); j++) {
      string s = dict[i];
      s[j] = '*';
      table[s].push_back(dict[i]);
    }
  }


  q.push(start);
  while(q.size() != 0) {
    string curr = q.front();
    q.pop();

    cout << curr << endl;
    if(curr == end)
      return true;

    for(int i = 0; i < (int)curr.length(); i++) {
      string s = curr;
      s[i] = '*';
      if(table[s].size() > 0) {
        for(int j = 0; j < (int)table[s].size(); j++) {
          if(!seen[table[s][j]]) {
            q.push(table[s][j]);
            seen[table[s][j]] = true;
          }
        }
      }
    }
  }

  return false;
}

int main()
{
  string start = "hit";
  string end = "cog";
  vector<string> dict;
  dict.push_back("hot");
  dict.push_back("dot");
  dict.push_back("dog");
  dict.push_back("lot");
  dict.push_back("log");
  cout << BFS(start, end, dict) << endl;
  return 0;
}
