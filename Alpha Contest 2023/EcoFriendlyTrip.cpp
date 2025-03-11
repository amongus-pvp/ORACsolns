/*
TRYING TO MINIMISE THESE. Hopefully this is the ONLY C++ solution i just cannot optimise for python
https://orac2.info/problem/1216/
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;
 
vector<vector<int>> preprocess_grid(const vector<vector<int>>& grid) {
    int n = grid.size();
    vector<vector<int>> prefix(n + 1, vector<int>(n + 1, 0));
    for (int r = 1; r <= n; ++r) {
        for (int c = 1; c <= n; ++c) {
            prefix[r][c] = grid[r - 1][c - 1] 
                           + prefix[r - 1][c] 
                           + prefix[r][c - 1] 
                           - prefix[r - 1][c - 1];
        }
    }
    return prefix;
}
 
inline int right_move_cost(const vector<vector<int>>& prefix, int n, int r, int c, int k_offset) {
    int col = c + 1 + k_offset;
    if (col >= n) return 0;
    int start_row = max(0, r - k_offset);
    int end_row = min(n, r + k_offset + 1);
    int r1 = start_row + 1;
    int r2 = end_row;
    int c1 = col + 1;
    int c2 = col + 1;
    return prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1];
}
 
inline int down_move_cost(const vector<vector<int>>& prefix, int n, int r, int c, int k_offset) {
    int row = r + 1 + k_offset;
    if (row >= n) return 0;
    int start_col = max(0, c - k_offset);
    int end_col = min(n, c + k_offset + 1);
    int r1 = row + 1;
    int r2 = row + 1;
    int c1 = start_col + 1;
    int c2 = end_col;
    return prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1];
}
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int n, k;
    cin >> n >> k;
    vector<vector<int>> grid(n, vector<int>(n));
    for (int r = 0; r < n; ++r)
        for (int c = 0; c < n; ++c)
            cin >> grid[r][c];
 
    vector<vector<int>> prefix = preprocess_grid(grid);
    int k_offset = (k - 1) / 2;
    
    // Use flat arrays for dp and parent
    vector<int> dp(n * n, numeric_limits<int>::max());
    vector<pair<int, int>> parent(n * n, {-1, -1});
    
    auto idx = [n](int r, int c) { return r * n + c; };
 
    // Calculate starting cost (using the same prefix-sum technique)
    int start_row = max(0, 0 - k_offset);
    int end_row = min(n, 0 + k_offset + 1);
    int start_col = max(0, 0 - k_offset);
    int end_col = min(n, 0 + k_offset + 1);
    int r1 = start_row + 1, r2 = end_row, c1 = start_col + 1, c2 = end_col;
    int start_cost = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1];
    dp[idx(0, 0)] = start_cost;
    
    // DP loop over all cells (only right and down moves)
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            int current = idx(r, c);
            // Right move
            if (c + 1 < n) {
                int cost = right_move_cost(prefix, n, r, c, k_offset);
                int next = idx(r, c + 1);
                if (dp[current] + cost < dp[next]) {
                    dp[next] = dp[current] + cost;
                    parent[next] = {r, c};
                }
            }
            // Down move
            if (r + 1 < n) {
                int cost = down_move_cost(prefix, n, r, c, k_offset);
                int next = idx(r + 1, c);
                if (dp[current] + cost < dp[next]) {
                    dp[next] = dp[current] + cost;
                    parent[next] = {r, c};
                }
            }
        }
    }
    
    cout << dp[idx(n - 1, n - 1)] << "\n";
    return 0;
}
