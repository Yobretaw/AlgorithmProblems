#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

// An independent set in a graph is a subset of vertices no two joined by an edge. Give an efficient dynamic programming algorithm to find the maximum weight of an independent set in a graph that is a path. In other words, the graph is an undirected graph of the form G = (V, E) where V = {1,...,n} and E = {(i,i+1) ∶ i = 1,...,n−1}; you are given a weight function w ∶ V → N, and the algorithm must find the maximum of w(U) where U is an independent set U ⊂ V. Recall that w(U) = ∑ w(v).

// vertices from 1 to n, n determined by the length of vector 'weight'
int find(vector<int> weight) {
  int n = weight.size();
  vector<vector<int> > table(weight.size(), vector<int>(weight.size()));
  vector<vector<int> > useEdge(weight.size(), vector<int>(weight.size()));

  for (int i = 0; i < n; i++) {
    table[i][i] = weight[i];
    useEdge[i][i] = 1;
  }

  // useEdge[i][j] = 1 if vertices #j is being used
  for (int i = 0; i < n-2; i++) {
    table[i][i+2] = weight[i] + weight[i+2];
    useEdge[i][i+2] = 1;
  }


  int maxWeight = -1;
  for (int len = 3; len <= n; len++) {
    for (int i = 0; i < n - len + 1; i++) {
      int j = i + len - 1;
      bool u = useEdge[i][j-1];
      
      if(u) {
        if(table[i][j-2] + weight[j] > table[i][j-1]) {
          useEdge[i][j] = 1;
          table[i][j] = table[i][j-2] + weight[j];
        } else {
          useEdge[i][j] = 0;
          table[i][j] = table[i][j-1];
        }
      } else {
        useEdge[i][j] = 1;
        table[i][j] = table[i][j-1] + weight[j];
      }

      if(table[i][j] > maxWeight)
        maxWeight = table[i][j];
    }
  }

  return maxWeight;
}

int main()
{
  vector<int> weight(10);

  weight.push_back(1);
  weight.push_back(1);
  weight.push_back(1);
  weight.push_back(1);
  weight.push_back(4);
  weight.push_back(1);
  weight.push_back(-5);
  weight.push_back(1);
  weight.push_back(1);
  weight.push_back(1);
  weight.push_back(1);

  cout << find(weight) << endl;
  return 0;
}
