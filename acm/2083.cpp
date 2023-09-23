#include <iostream>

int main() {
    while (true) {
        std::string name;
        int age, weight;
        
        std::cin >> name;
        std::cin >> age;
        std::cin >> weight;
        
        if (name == "#") break;
        
        std::string type = (age > 17 || weight >= 80) ? " Senior" : " Junior";
        
        std::cout << name + type << std::endl;
    }
}