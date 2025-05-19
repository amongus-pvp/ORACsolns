// https://orac2.info/problem/1/
// tried rewriting in python, too slow on 2 testcases, not even AI could optimise the python code so I'm js gonna give up

#include <bits/stdc++.h>
using namespace std;
 
const int MOD = 1000003;
const int MAXN = 1000;
int R, C;
int grid[MAXN][MAXN];
int dp[MAXN][MAXN];
bool is_max[MAXN][MAXN];
bool is_min[MAXN][MAXN];
 
vector<pair<int, pair<int, int>>> cells;
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    freopen("birdin.txt", "r", stdin);
    freopen("birdout.txt", "w", stdout);
 
    cin >> R >> C;
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            cin >> grid[i][j];
 
    // Directions: up, down, left, right
    const int dx[4] = {-1, 1, 0, 0};
    const int dy[4] = {0, 0, -1, 1};
 
    // Identify local maxima and minima
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            bool maxima = true, minima = true;
            int h = grid[i][j];
            for (int d = 0; d < 4; ++d) {
                int ni = i + dx[d], nj = j + dy[d];
                if (ni >= 0 && ni < R && nj >= 0 && nj < C) {
                    if (grid[ni][nj] > h) maxima = false;
                    if (grid[ni][nj] < h) minima = false;
                }
            }
            is_max[i][j] = maxima;
            is_min[i][j] = minima;
            cells.emplace_back(-grid[i][j], make_pair(i, j));  // sort descending
        }
    }
 
    sort(cells.begin(), cells.end());
 
    int total = 0;
 
    for (auto& cell : cells) {
        int i = cell.second.first, j = cell.second.second;
        if (is_max[i][j]) dp[i][j] = 1;
        for (int d = 0; d < 4; ++d) {
            int ni = i + dx[d], nj = j + dy[d];
            if (ni >= 0 && ni < R && nj >= 0 && nj < C) {
                if (grid[ni][nj] < grid[i][j]) {
                    dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD;
                }
            }
        }
        if (is_min[i][j]) {
            total = (total + dp[i][j]) % MOD;
        }
    }
 
    cout << total << '\n';
    return 0;
}
