// https://orac2.info/problem/1538/

// 53.44 points

#include "arrayser.h"
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;
 
void play_arrayser(int N) {
    vector<int> A(N, 1);  // Initialize array A with 1s
 
    // Helper function to check if a given index is valid
    auto is_valid = [&](int i) {
        return i >= 0 && i < N && A[i] == 1;
    };
 
    // Helper function to set a given index and its neighbors to 0
    auto make_move = [&](int i) {
        A[i] = 0;
        if (i - 1 >= 0) A[i - 1] = 0;
        if (i + 1 < N) A[i + 1] = 0;
    };
 
    int last_friend_move = -1;
 
    while (true) {
        int move = -1;
        int max_priority = -1;
 
        // We now evaluate moves based on their potential to keep the game going
        for (int i = 0; i < N; ++i) {
            if (A[i] == 1) {
                int left_gap = (i > 0 && A[i - 1] == 0) ? 1 : 0;
                int right_gap = (i < N - 1 && A[i + 1] == 0) ? 1 : 0;
                int cluster_size = 1;
 
                // Count the cluster size to the right
                int j = i + 1;
                while (j < N && A[j] == 1) {
                    cluster_size++;
                    j++;
                }
 
                // Priority based on cluster size and gaps
                int priority = cluster_size * 2 - (left_gap + right_gap);
 
                // Increase priority for larger clusters
                if (cluster_size > 5) priority += 3;
                if (cluster_size > 10) priority += 5;
 
                // Penalize moves that would immediately finish the game
                if (cluster_size == N) priority -= 10;
 
                // Choose the middle of a large cluster if possible
                if (cluster_size > 1) priority += abs(cluster_size / 2 - (i - (j - cluster_size)));
 
                if (priority > max_priority) {
                    max_priority = priority;
                    move = i;
                }
 
                i = j - 1;  // Skip to the end of the cluster
            }
        }
 
        if (move == -1) return;  // No valid moves left
 
        // Make our move
        last_friend_move = do_turn(move);
 
        // Apply the move effects
        make_move(move);
 
        // If the friend made the final move, end the game
        if (last_friend_move == -1) return;
 
        // Apply friend's move effects
        make_move(last_friend_move);
    }
}