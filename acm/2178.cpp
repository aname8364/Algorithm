#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

vector<vector<int>> bfs(const vector<vector<int>>& maze, int start_x, int start_y, int n, int m) {
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    queue<pair<int, int>> q;
    vector<vector<int>> dist(n, vector<int>(m, 0));
    
    q.push({start_x, start_y});
    visited[start_x][start_y] = true;
    dist[start_x][start_y]++;
    
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for (int i=0; i<4; i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            
            if (new_x < 0 || new_x >= n || new_y < 0 || new_y >= m) { continue; }
            
            if (maze[new_x][new_y] == 1 && !visited[new_x][new_y]) {
                q.push({new_x, new_y});
                visited[new_x][new_y] = true;
                dist[new_x][new_y] = dist[x][y] + 1;
            }
        }
    }
    return dist;
}

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> maze(n, vector<int>(m));
    
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            char cell;
            cin >> cell;
            maze[i][j] = cell - '0';
        }
    }
    
    vector<vector<int>> dist = bfs(maze, 0, 0, n, m); // bad impl
    // need fix bad index
    cout << dist[n-1][m-1];
    
}
