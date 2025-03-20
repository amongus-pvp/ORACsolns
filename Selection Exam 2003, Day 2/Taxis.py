# https://orac2.info/problem/88/
def main():
    # Read input from file
    with open("taxiin.txt", "r") as file:
        data = file.read().split()
    
    # Parse the number of students (s) and the number of taxi types (n)
    s = int(data[0])
    n = int(data[1])
    
    # Parse the taxi types (cost and seats)
    taxis = []
    index = 2
    for _ in range(n):
        cost = int(data[index])
        seats = int(data[index + 1])
        taxis.append((cost, seats))
        index += 2
    
    # Initialize the DP array
    dp = [float('inf')] * (s + 1)
    dp[0] = 0  # Cost to transport 0 students is 0
    
    # Update the DP array for each number of students
    for i in range(s + 1):
        if dp[i] != float('inf'):
            for cost, seats in taxis:
                # Case 1: Fill the taxi completely
                if i + seats <= s:
                    dp[i + seats] = min(dp[i + seats], dp[i] + cost)
                # Case 2: Fill the taxi with one empty seat
                if i + seats - 1 <= s and seats - 1 >= 0:
                    dp[i + seats - 1] = min(dp[i + seats - 1], dp[i] + cost)
    
    # Write the result to the output file
    with open("taxiout.txt", "w") as file:
        file.write(str(dp[s]))
 
if __name__ == "__main__":
    main()