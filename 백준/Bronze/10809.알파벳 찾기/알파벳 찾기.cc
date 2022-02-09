#include <iostream>
#include <string>
using namespace std;

int main() {
	int alphabet[26];
	fill_n(alphabet, 26, -1);

	string s;
	cin >> s;

	for (int i = 0; i < s.length(); i++) {
		char ch = 97;
		while (ch <= 122) {
			if (s[i] == ch) {
				if (alphabet[ch - 97] == -1)
					alphabet[ch - 97] = i;
				break;
			}
			ch++;
		}
	}
	
	for (auto e : alphabet)
		cout << e << " ";
}