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

/*
 *  Given numRows, generate the first numRows of Pascal's triangle.
 *  
 *  For example, given numRows = 5, return
 *  [
 *       [1],
 *      [1,1],
 *     [1,2,1],
 *    [1,3,3,1],
 *   [1,4,6,4,1]
 *  ]
 */
vector<vector<int> > generate(int numRows) {
  vector<vector<int> > result(numRows);
  if(numRows == 0) return result;

  for(int i = 0; i < numRows; ++i) {
    result[i] = vector<int>(i + 1);
    result[i][0] = 1;
    result[i][i] = 1;
    for(int j = 1; j < i; ++j) {
      result[i][j] = result[i - 1][j - 1] + result[i - 1][j];
    }
  }
  return result;
}

vector<int> generateKthRow(int k) {
  vector<int> result(k + 1, 1);
  if(k == 0) return result;

  result[0] = 1;
  result[k] = 1;

  vector<int> aboveRow(result);
  for(int i = 0; i <= k; ++i) {
    for(int j = 1; j < i; ++j) {
      result[j] = aboveRow[j - 1] + aboveRow[j];
    }
    aboveRow = result;
  }
  return result;
}

vector<int> generateKthRow2(int k) {
  vector<int> row;
  for(int i = 0; i <= k; ++i) {
     for(int j = i - 1; j > 0; --j)
       row[j] = row[j - 1] + row[j];
     row.push_back(1);
  }
  return row;
}

int main() {
  vector<vector<int> > result = generate(5);
  for(auto row : result) {
    for(auto val : row) cout << val << " ";
    cout << endl;
  }
  vector<int> result2 = generateKthRow(4);
  for(auto val : result2) cout << val << " ";
  return 0;
}
