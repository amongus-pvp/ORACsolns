// https://orac2.info/problem/1537/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
const int MAXN = 500005;
const int INF = 1e9;
 
vector<int> children[MAXN];
int weight[MAXN];
vector<int> adj[MAXN]; // Adjacency list for reachable nodes
ll totalSum = 0;
 
// DFS to compute min and max descendants
pair<int, int> dfs1(int node, int min_ancestor, int max_ancestor) {
    int min_descendant = INF, max_descendant = -INF;
    for (int child : children[node]) {
        auto [min_child, max_child] = dfs1(child, min(min_ancestor, node), max(max_ancestor, node));
        min_descendant = min(min_descendant, min_child);
        max_descendant = max(max_descendant, max_child);
    }
    set<int> raw_adj = {min_descendant, max_descendant, min_ancestor, max_ancestor};
    for (int neighbor : raw_adj) {
        if (abs(neighbor) != INF) {
            adj[node].push_back(neighbor);
        }
    }
    return {min(node, min_descendant), max(node, max_descendant)};
}
 
// DFS to compute reachable nodes and sum their weights
void dfs2(int node, vector<bool>& visited, ll& sum) {
    visited[node] = true;
    sum += weight[node];
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs2(neighbor, visited, sum);
        }
    }
}
 
int main() {
    int N, R;
    cin >> N >> R;
    for (int i = 1; i <= N; ++i) {
        int parent;
        cin >> parent;
        if (parent != 0) {
            children[parent].push_back(i);
        }
    }
    for (int i = 1; i <= N; ++i) {
        cin >> weight[i];
    }
 
    // Compute min and max descendants
    dfs1(R, INF, -INF);
 
    // Compute reachable nodes and sum their weights
    for (int u = 1; u <= N; ++u) {
        ll sum = 0;
        vector<bool> visited(N + 1, false);
        dfs2(u, visited, sum);
        totalSum += weight[u] * (sum - weight[u]);
    }
 
    cout << totalSum << endl;
 
    return 0;
}