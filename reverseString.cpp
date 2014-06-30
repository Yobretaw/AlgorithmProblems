/*
 *
 * Given an input string, reverse the string word by word.

    For example,
    Given s = "the sky is blue",
    return "blue is sky the".
    
    click to show clarification.
    
    Clarification:
    What constitutes a word?
     - A sequence of non-space characters constitutes a word.

    Could the input string contain leading or trailing spaces?
     - Yes. However, your reversed string should not contain leading or trailing spaces.

    How about multiple spaces between two words?
     - Reduce them to a single space in the reversed string.
 */

#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

void reverseWords(string& s);
int getNextIndex(string s, int i);

int main(int argc, const char *argv[])
{
    //string a = "       abbaa    b  ";
    string a = "hi!";
    reverseWords(a);
    cout << "!!!" << a << "!!!" << endl;
    cout << a.length() << endl;
    for (int i = 0; i < a.length(); i++) {
        cout << a[i] << endl;
    }
    return 0;
}

int getNextIndex(string s, int i) {
    while(s[i] == ' ') i--;
    return i;
}

void reverseWords(string& s) {
    string retval = "";
    int i = getNextIndex(s, s.length()-1);
    if (i < 0) {
        s = "";
    }

    while(i >= 0) {
        i = getNextIndex(s, i);
        if(retval != "" && i < s.length() -1 && s[i+1] == ' ') retval += " ";

        string part = "";
        while(i >= 0 && s[i] != ' ') {
            part = s[i] + part;
            i--;
        }
        retval += part;
    }
    if(i == 0 && s[0] != ' ') retval += s[0];
    s = retval;
}

