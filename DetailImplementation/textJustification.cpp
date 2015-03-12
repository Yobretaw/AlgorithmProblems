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
 *  Given an array of words and a length L, format the text such that each line has exactly L characters and
 *  is fully (left and right) justified.
 *  
 *  You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
 *  Pad extra spaces ' ' when necessary so that each line has exactly L characters.
 *  
 *  Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line
 *  do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
 *  
 *  For the last line of text, it should be left justified and no extra space is inserted between words.
 *  
 *  For example,
 *  words: ["This", "is", "an", "example", "of", "text", "justification."]
 *  L: 16.
 *  
 *  Return the formatted lines as:
 *  [
 *     "This    is    an",
 *     "example  of text",
 *     "justification.  "
 *  ]
 *  Note: Each word is guaranteed not to exceed L in length.
 *  
 *  Corner Cases:
 *  A line other than the last line might contain only one word. What should you do in this case?
 *  In this case, that line should be left-justified.
 */
vector<string> justify(const vector<string>& words, int L) {
  int wordCount = words.size();

  if(wordCount == 0) {
    return vector<string>{ string(' ', L) };
  }

  if(wordCount == 1) {
    vector<string> ret = { words[0] };
    while(ret[0].length() < L) ret[0] += " ";
    return ret;
  }

  vector<vector<string> > lines;
  int idx = 0;
  int linecount = 0;
  while(idx < wordCount) {
    if(words[idx].length() == L) {
      lines.push_back(vector<string>{words[idx++]});
      continue;
    }

    vector<string> lastline;
    int totalLen = 0;
    while(totalLen + words[idx].length() < L) {
      if(!lastline.empty()) {
        totalLen += 1;
      }
      lastline.push_back(words[idx]);
      totalLen += words[idx].length();
      idx++;
    }
    lines.push_back(lastline);
  }

  // construction lines
  vector<string> result;
  for(int idx = 0; idx < lines.size(); ++idx) {
    vector<string> line = lines[idx];

    int linelength = 0;
    for(auto str : line)
      linelength += str.length();
    int whitespace = line.size() == 1 ? L - linelength : (L - linelength) / (line.size() - 1);
    int extra = line.size() == 1 ? 0 : (L - linelength) % (line.size() - 1);

    string linestr = "";
    for(int i = 0; i < line.size(); ++i) {
      linestr += line[i];
      if(idx == lines.size() - 1) {
         if(linestr.length() < L) linestr += " ";
         continue;
      }
      if(i != line.size() - 1) {
        linestr += string(whitespace, ' ');
        if(extra-- > 0) linestr += " ";
      }
    }
    if(linestr.length() < L) linestr += string(L - linestr.length(), ' ');
    result.push_back(linestr);
  }
  return result;
}

int main() {
  vector<string> words = {
    //"This", "is", "an", "example", "of", "text", "justification.",
    "a", "b", "c", "d", "e"
  };
  vector<string> result = justify(words, 3);
  for(auto line : result) {
     cout <<  "\"" << line << "\""  << endl;
  }
  return 0;
}
