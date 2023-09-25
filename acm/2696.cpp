#include <iostream>
#include <queue>

using namespace std;

int main() {
    int T;
    cin >> T;
    
    for (int i=0; i<T; i++) {
        int M;
        cin >> M;
        
        priority_queue<int, vector<int>, less<int>>     max_pq;
        priority_queue<int, vector<int>, greater<int>>  min_pq;
        
        vector<int> median;
        
        for (int j=1; j<=M; j++) { // <-- i번째 수로 통일
            int x;
            cin >> x;
            
            if (j%2!=0) {
                // 홀수일때
                max_pq.push(x);
                if (!max_pq.empty() && !min_pq.empty()) {
                    int max_top = max_pq.top();
                    int min_top = min_pq.top();
                    
                    if (max_top > min_top) {
                        min_pq.push(max_top);
                        max_pq.pop();
                        
                        max_pq.push(min_top);
                        min_pq.pop();
                    }
                }
                median.push_back(max_pq.top());
            }
            else { min_pq.push(x); }
        }
        
        cout << median.size() << "\n";
        for (int x: median) {
            cout << x << " ";
        }
        cout << "\n";
    }
}