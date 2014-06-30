// ===============================================================
// Find the longest palindrome substring//
// LANG: C++
// Run Time: O(n)
// ===============================================================
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

string longestPalSubstring(string s);
string helper(string s);

/*
string operator*( int n, string s ) {
        string s1 = ""
        for( int i = 0  i < n i++ )
                for( int j = 0 j < s.length() j++ )
                        s1 += s[j]
        return s1
}     
*/

string longestPalSubstring( string s ) {
        // [maxCenter]: the maxCenter of the longest palindrome 
        // substring
        // [radius]: the length that substring extends
	string input = "";
	for(int i = 0; i < s.length(); i++) {
		input += "#";
		input += s[i];
	}
	input += "#";
	return helper(input);
}

string helper(string s) {
	int radius = 0;
	int maxCenter = 0;
        int rightEnd = 0;
	int currCenter = 0;

        // inialize a int array with length equal to the
        // length of given string, and set all entries
        // to 0
        int p[s.length()];
        memset(p, 0, sizeof(p));

        for( int i = 1; i < s.length(); i++ ) {

                p[i] = (rightEnd > i) ? min( p[2*currCenter-i], rightEnd-i ):1;
                
                // compare two chars in boarders of the substring
                // maxCentered at i
                while(s[i + p[i]] == s[i - p[i]]) {
                        p[i]++;
                }
		
                if( i + p[i] > rightEnd ) {
                        rightEnd = i + p[i];
                        currCenter = i;
                }
		if(p[i] > radius) {
			radius = p[i];
			maxCenter = i;
		}
        }

	if(radius <= 2) {
		return "";
	}
	string retval = "";
	for(int i = maxCenter - radius + 2; i <= maxCenter + radius - 2; i+=2) {
		retval += s[i];
	}
	return retval;
}

int main() {
	string a = "aa";
	cout << longestPalSubstring(a) << endl;
	return 0;
}
