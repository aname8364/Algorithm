#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

int dfs(const vector<vector<int>>& maze, vector<vector<bool>>& visited, int start_x, int start_y, int n) {
    stack<pair<int, int>> st;
    int count = 0;
    
    st.push({start_x, start_y});
    visited[start_x][start_y] = true;
    
    while (!st.empty()) {
        int x = st.top().first;
        int y = st.top().second;
        st.pop();
        count++;
        
        for (int i=0; i<4; i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            
            if (new_x < 0 || new_x >= n || new_y < 0 || new_y >= n) { continue; }
            
            if (maze[new_x][new_y] == 1 && !visited[new_x][new_y]) {
                st.push({new_x, new_y});
                visited[new_x][new_y] = true;
            }
        }
    }
    return count;
}

int main() {
    int n;
    cin >> n;
    
    vector<vector<int>> maze(n+1, vector<int>(n+1));
    vector<vector<bool>> visited(n+1, vector<bool>(n+1, false));
    
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            char cell;
            cin >> cell;
            maze[i][j] = cell - '0';
        }
    }
    
    vector<int> homes;
    //homes.reserve(n*n);
    
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            if (maze[i][j] != 0 && !visited[i][j]) { homes.emplace_back(dfs(maze, visited, i, j, n)); }
        }
    }
    
    sort(homes.begin(), homes.end());
    
    size_t size = homes.size();
    cout << size << "\n";
    for (auto n: homes) { cout << n << "\n"; }
}
