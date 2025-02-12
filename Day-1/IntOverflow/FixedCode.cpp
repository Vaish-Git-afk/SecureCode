#include <iostream>
#include <limits>

bool safe_add(int a, int b, int &result) {
    if ((b > 0 && a > std::numeric_limits<int>::max() - b) || 
        (b < 0 && a < std::numeric_limits<int>::min() - b)) {
        return false; // Overflow detected
    }
    result = a + b;
    return true;
}

int main() {
    int x = 294967296;
    int y = 40000000001; 
    int result;

    if (safe_add(x, y, result)) {
        std::cout << "Result: " << result << std::endl;
    } else {
        std::cout << "Error: Overflow detected!" << std::endl;
    }

    return 0;
}