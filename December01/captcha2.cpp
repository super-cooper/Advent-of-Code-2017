#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<int> puzzle;
    string input;
    cin >> input;
    for (char c : input) {
        puzzle.push_back((int) strtol(&c, nullptr, 10));
    }
    int count = 0;
    unsigned long n = puzzle.size();
    for (int i = 0; i < n/2 ; i++) {
        if (puzzle[i] == puzzle[i + n/2]) {
            count += puzzle[i];
        }
    }
    cout << (2 * count) << endl;
}
