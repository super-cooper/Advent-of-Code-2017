#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int i = 1;
    int x = 0;
    int y = 0;
    int row = 1;
    bool solved = false;

    while (i < n) {
        while (x < row && !solved) {
            x++;
            solved = ++i == n;
        }
        while (y < row && !solved) {
            y++;
            solved = ++i == n;
        }
        while (x > -row && !solved) {
            x--;
            solved = ++i == n;
        }
        while (y > -row && !solved) {
            y--;
            solved = ++i == n;
        }
        row++;
    }
    std::cout << (abs(x) + abs(y)) << std::endl;
}