#include <iostream>

int replace_all(std::string& s, const std::string& target, const std::string& to) {
    int count = 0;
    size_t found = s.find(target);
    while (found != std::string::npos) {
        count++;
        s.replace(found, target.length(), to);
        found = s.find(target, found+1);
    }
    return count;
}

int main() {
    int n;
    std::cin >> n;
    
    for (int i=0; i<n; i++) {
        std::string s;
        std::cin >> s;
        
        int count = 0;
        
        count += replace_all(s, "@", "a");
        count += replace_all(s, "[", "c");
        count += replace_all(s, "!", "i");
        
        count += replace_all(s, ";", "j");
        count += replace_all(s, "^", "n");
        count += replace_all(s, "0", "o");
        
        count += replace_all(s, "7", "t");
        count += replace_all(s, "\\\\'", "w");
        count += replace_all(s, "\\'", "v");
        
        if (count >= s.length()/2.0) {
            std::cout << "I don't understand" << std::endl;
            continue;
        }
        
        std::cout << s << std::endl;
    }
}