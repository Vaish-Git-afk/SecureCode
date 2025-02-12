#include <iostream>
#include <limits>

int add(int a, int b) {
    return a + b;
}

int main() {
    int x,y;
    std::cout << "Enter the first integer (x): ";
    std::cin >> x;
    std::cout << "Enter the second integer (y): ";
    std::cin >> y;
    int result = add(x, y);  
    std::cout << "Result: " << result << std::endl;
    return 0;
}


/* 
Output
------ 
Enter the first integer (x): 294967296
Enter the second integer (y): 40000000001
Result: -1852516353

*/