# https://orac2.info/problem/167/
import sys
 
# Reading from file
sys.stdin = open("convin.txt", "r")
sys.stdout = open("convout.txt", "w")
 
 
def main():
    n = int(input())
    desired_order = [int(input()) for _ in range(n)]
 
    queue1 = []  # Queue 1 for boxes
    queue2 = []  # Queue 2 for boxes
    result = []  # To store the output (1 or 2)
 
    # Track the current position for both queues
    last1, last2 = -1, -1
 
    for i in range(n):
        box = desired_order[i]
 
        # Check if the current box can be added to either queue while maintaining order
        add_to_queue1 = (last1 == -1 or last1 < box)
        add_to_queue2 = (last2 == -1 or last2 < box)
 
        # Prioritize adding to queue 1 if both are valid
        if add_to_queue1 and (not add_to_queue2 or (queue1 and box <= queue1[-1])):
            queue1.append(box)
            last1 = box
            result.append(1)
        elif add_to_queue2:
            queue2.append(box)
            last2 = box
            result.append(2)
 
    for r in result:
        print(r)
 
if __name__ == '__main__':
    main()