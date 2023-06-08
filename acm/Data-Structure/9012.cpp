#include <iostream>
#include <string>
#include <stack>

bool check_vps(const std::string& ps) {
    std::stack<char> stack;
    for (char c: ps) {
        if (c == '(') {
            stack.push(c);
        }
        else if (c == ')') {
            if (stack.empty()) {
                return false;
            }
            stack.pop();
        }
    }
    return stack.empty();
}

int main() {
    int case_count;
    std::cin >> case_count;

    for (int i=0; i<case_count; i++) {
        std::string testcase;
        std::cin >> testcase;
        std::cout << (check_vps(testcase) ? "YES" : "NO") << "\n";
    }
}