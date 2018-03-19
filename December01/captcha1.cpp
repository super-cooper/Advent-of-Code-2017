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
    for (int i = 0; i < puzzle.size() - 1; i++) {
        if (puzzle[i] == puzzle[i + 1]) {
            count += puzzle[i];
        }
    }
    if (puzzle[puzzle.size() - 1] == puzzle[0])
        count += puzzle[0];
    cout << count << endl;
}
