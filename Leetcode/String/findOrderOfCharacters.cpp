#include "string"
#include "stack"
#include "vector"
#include "map"
#include "stdio.h"
using namespace std;

class Graph {
  int v;
  vector<char> ch;
  map<char, vector<char> > adj;
  void sortHelp(char v, bool visited[], stack<char>& s);

  public:
  Graph(int v) {
    this->v = v;

    for(int i = 0; i < v; i++) 
      ch.push_back('a' + i);
  }

  void addEdge(char v, char w);
  void sort();
};

void Graph::addEdge(char v, char w) {
  this->adj[v].push_back(w);
}

void Graph::sortHelp(char v, bool visited[], stack<char>& s) {
  visited[v - 'a'] = true; 

  for(int i = 0; i < (int)this->adj[v].size(); i++) {
    if(!visited[this->adj[v][i] - 'a']) {
      sortHelp(this->adj[v][i], visited, s);
    }
  }

  s.push(v);
}

void Graph::sort() {
  stack<char> s;

  bool* visited = new bool[ch.size()];
  for(int i = 0; i < (int)ch.size(); i++)
    visited[i] = false;

  for(int i = 0; i < v; i++) {
    if(visited[i] == false) {
      sortHelp(ch[i], visited, s);
    }
  }

  while(s.empty() == false) {
    printf("%c", s.top());
    s.pop();
  }
}

void printOrder(vector<string> words, int alpha) {
  Graph g(alpha);

  for(int i = 0; i < alpha; i++) {
    string word1 = words[i];
    string word2 = words[i+1];

    for(int j = 0; j < (int)min(word1.length(), word2.length()); j++) {
      if(word1[j] != word2[j]) {
        g.addEdge(word1[j], word2[j]);
        break;
      }
    }
  }

  g.sort();
}

int main()
{
  vector<string> v; 
  v.push_back("baa");
  v.push_back("abcd");
  v.push_back("abca");
  v.push_back("cab");
  v.push_back("cad");
  v.push_back("ecad");

  printOrder(v, 5);
  return 0;
}
