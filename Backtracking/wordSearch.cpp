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
 * Given a 2D board and a word, find if the word exists in the grid.
 * 
 * The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
 * 
 * For example, given board =
 * 
 *   [
 *     ["ABCE"],
 *     ["SFCS"],
 *     ["ADEE"]
 *   ]
 * 
 *   word = "ABCCED", -> returns true,
 *   word = "SEE", -> returns true,
 *   word = "ABCB", -> returns false.
 */

bool searchHelp(const vector<vector<char> >& grid, string word, int curr, int x, int y, vector<vector<bool> >& used) {
  if(x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size())
    return false;

  if(curr == word.length() - 1)
    return !used[x][y] && grid[x][y] == word[curr];

  if(grid[x][y] != word[curr] || used[x][y]) return false;

  used[x][y] = true;
  bool next = searchHelp(grid, word, curr + 1, x - 1, y, used) ||
    searchHelp(grid, word, curr + 1, x, y - 1, used) ||
    searchHelp(grid, word, curr + 1, x + 1, y, used) ||
    searchHelp(grid, word, curr + 1, x, y + 1, used);

  used[x][y] = false;
  return next;
}

bool search(const vector<vector<char> >& grid, string word) {
  vector<vector<bool> > used(grid.size(), vector<bool>(grid[0].size(), false));
  for (int i = 0; i < grid.size(); ++i) {
    for (int j = 0; j < grid[i].size(); ++j) {
      if(grid[i][j] != word[0]) continue;
      if(searchHelp(grid, word, 0, i, j, used))
        return true;
    }
  }
  return false;
}

int main() {
  vector<vector<char> > grid = {
    {'A', 'B', 'C', 'E'},
    {'S', 'F', 'C', 'S'},
    {'A', 'D', 'E', 'E'}
  };
  cout << search(grid, "ABCCED") << endl;
  cout << search(grid, "SEE") << endl;
  cout << search(grid, "ABCB") << endl;
  cout << search(grid, "ABCESEEDASFC") << endl;
  return 0;
}
