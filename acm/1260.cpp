#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

void dfs(int x, const vector<int> adj[], bool visited[]) {
    visited[x] = true;
    cout << x << " ";
    
    for (auto y: adj[x]) {
        if (!visited[y]) { dfs(y, adj, visited); }
    }
}

void bfs(const vector<int> adj[], int start, int n) {
    vector<bool> visited(n, false);
    queue<int> q;
    
    q.push(start);
    
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        
        if (!visited[x]) {
            visited[x] = true;
            cout << x << " ";
            
            for (int y : adj[x]) {
                if (!visited[y]) {
                    q.push(y);
                }
            }
        }
    }
}

int main() {
    int n, m, v;
    cin >> n >> m >> v;
    
    vector<int> adj[n+1];
    bool visited[n+1];
    
    for (int i=0; i<m; i++) {
        int first_vertex, next_vertex;
        cin >> first_vertex >> next_vertex;
        
        adj[first_vertex].emplace_back(next_vertex);
        adj[next_vertex].emplace_back(first_vertex);
    }
    
    for (int i = 1; i <= n; i++) {
        visited[i] = false;
        sort(adj[i].begin(), adj[i].end());
    }
    
    dfs(v, adj, visited);
    cout << "\n";
    bfs(adj, v, n); 
}
